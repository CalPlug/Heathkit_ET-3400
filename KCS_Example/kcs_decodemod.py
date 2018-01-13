#!/usr/bin/env python3
# kcs_decode.py
#
# Author : David Beazley (http://www.dabeaz.com)
# Modified by: Michael John Klopfer, Ph.D., Univ. of California, Irvine
# Original Copyright (C) 2010
# Modified (C) 2017
#
# Requires Python 3.1.2 or newer

"""
Converts a WAV file containing Kansas City Standard data and
extracts text data from it. See:

http://en.wikipedia.org/wiki/Kansas_City_standard
"""

from collections import deque
from itertools import islice

# Generate a sequence representing sign bits
def generate_wav_sign_change_bits(wavefile):
    samplewidth = wavefile.getsampwidth()
    nchannels = wavefile.getnchannels()
    previous = 0
    while True:
        frames = wavefile.readframes(8192)
        if not frames:
            break

        # Extract most significant bytes from left-most audio channel
        msbytes = bytearray(frames[samplewidth-1::samplewidth*nchannels])

        # Emit a stream of sign-change bits
        for byte in msbytes:
            signbit = byte & 0x80
            yield 1 if (signbit ^ previous) else 0
            previous = signbit

# Base frequency (representing a 1)
BASE_FREQ = 2400

# Generate a sequence of data bytes by sampling the stream of sign change bits
def generate_bytes(bitstream,framerate):
    bitmasks = [0x1,0x2,0x4,0x8,0x10,0x20,0x40,0x80]

    # Compute the number of audio frames used to encode a single data bit
    frames_per_bit = int(round(float(framerate)*8/BASE_FREQ))

    # Queue of sampled sign bits
    sample = deque(maxlen=frames_per_bit)     

    # Fill the sample buffer with an initial set of data
    sample.extend(islice(bitstream,frames_per_bit-1))
    sign_changes = sum(sample)

    # Look for the start bit
    for val in bitstream:
        if val:
            sign_changes += 1
        if sample.popleft():
            sign_changes -= 1
        sample.append(val)

        # If a start bit detected, sample the next 8 data bits
        if sign_changes <= 9:
            byteval = 0
            for mask in bitmasks:
                if sum(islice(bitstream,frames_per_bit)) >= 12:
                    byteval |= mask
            yield byteval
            # Skip the final two stop bits and refill the sample buffer 
            sample.extend(islice(bitstream,2*frames_per_bit,3*frames_per_bit-1))
            sign_changes = sum(sample)

if __name__ == '__main__':
    import wave
    import sys
    import optparse

    p = optparse.OptionParser()
    p.add_option("-b",action="store_true",dest="binary")
    p.add_option("--binary",action="store_true",dest="binary")
    p.add_option("-f", "--file",
                  action="store", type="string", dest="filename",
                  help="write output to a FILE using --fOutputFileName.xxx ", metavar="FILE")
    p.set_defaults(binary=False) #display to console as default option with non binary formatting
    p.set_defaults(filename=False) #write displayed file contents to 

    opts, args = p.parse_args()
    if len(args) != 1 | len(args) != 2: #baseline fail with info (graceful) if garbage is entered to the command to run the script
        print("Usage: %s [-b] infile" % sys.argv[0],file=sys.stderr)
        print ("Arguments Used: %s" % len(args))
        raise SystemExit(1)

    wf = wave.open(args[0])
    sign_changes = generate_wav_sign_change_bits(wf)
    byte_stream  = generate_bytes(sign_changes, wf.getframerate())
    if (opts.filename):
        print ("Opening %s to write..." % opts.filename) # Remember, this will only write if in default mode (not binary)
        file_output = open(opts.filename, 'wb') # create a writeable file and write the decoding result, this opens the file to write into later

    if opts.binary:
        # Output the byte stream in 80-byte chunks with NULL stripping
        outf = sys.stdout.buffer.raw
        while True:
            buffer = bytes(islice(byte_stream,80))
            if not buffer:
                break
            outf.write(buffer)
    else:
        buffer = bytearray()
        while True:
            linebreak = buffer.find(b'\n')
            if linebreak >= 0:
                line = buffer[:linebreak+1].replace(b'\r\n',b'\n')
                sys.stdout.write(line.decode('latin-1')) #This is where the console display line typically comes from
                if opts.filename:
                    file_output.write(line) #Write a single line to the file if writing is enabled, this is the default usage mode
                del buffer[:linebreak+1]
                
            else:
                fragment = bytes(byte for byte in islice(byte_stream,80) if byte)
                if not fragment:
                    sys.stdout.write(buffer.decode('latin-1')) #Note, there is no output to file function available for binary mode, you will end up with a blank file.
                    break
                buffer.extend(fragment)
    if opts.filename:
        file_output.close()  #Close output file after completing write if writing is enabled
