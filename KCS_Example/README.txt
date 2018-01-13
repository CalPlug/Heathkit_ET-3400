py-kcs v1.1- Encode/Decode Kansas City Standard Audio Cassette Data

, Update for Binary File Encoding and Decoding

This original script for KCS interchange was built by 
Author: David Beazley (http://www.dabeaz.com)

Copyright (C) 2010 

Update by Michael Klopfer, UC Irvine, (C) 2017

This work extends on David Beazley's project to allow KCS encoding of binary files by using a Base64 encode and decode step.  

The workflow is shown as follows:

To Encode a binary file:
python base64enc.py smiley.jpg smiley.raw  //This takes the original binary file and encodes it to an ASCII Base 64 file
python kcs_encode.py smiley.raw output.wav //This encodes the ASCII file in KCS format audio

(This file would be recorded onto a tape, transferred, rerecorded back to an identical (nearly) audio file [*.WAV file, Mono, 9600 Hz Samp. Rate, 76kbps].

To Decode the audio for a binary file (you need to know the file type/extension):
python kcs_decodemod.py output.wav -fsmiley_decode.raw  //This decodes the ASCII (Base-64) file from the input KCS format audio
python base64dec.py smiley_decode.raw smiley_decode.jpg  //This decodes the original binary file and from the ASCII Base 64 file.  This is your original file




Here is David's original README Contents:



This is free software. You are free to use it however you wish, but if you
 decide to include it in some other package, please give me some credit.



Overview
--------
This package provides a pair of scripts, kcs_encode.py and kcs_decode.py
that encode and decode WAV audio files containing data encoded in the
Kansas City Standard as used on some of the first home computers.  In my
case, an Ohio Scientific Superboard II from 1978.  For more information
on KCS encoding, see http://en.wikipedia.org/wiki/Kansas_City_standard

Usage
-----
First of all, you need to install Python-3.1.2 or newer on your system.

To encode a text file into a WAV file suitable for playback, do this:

    % python3 kcs_encode.py input.txt output.wav

This reads the file 'input.txt' and writes a WAV file 'output.wav'. The
resulting WAV file is encoded in mono with a framerate of 9600 Hz.

To decode a WAV file containing KCS data that you have recorded, do
this:

    % python3 kcs_decode.py input.wav

Decoded text contained in the WAV file will be printed to standard
output.  This decoding process will strip NULL bytes and convert 
line endings to the native line endings for your platform.

If you want to decode raw binary data, type this:

    % python3 kcs_decode.py -b input.wav

In this case, output is still directed to standard output, but
is exactly as found in the audio (including all NULL bytes).

More Information
----------------
See the following blog posts for more information:

http://dabeaz.blogspot.com/2010/08/using-python-to-encode-cassette.html
http://dabeaz.blogspot.com/2010/08/decoding-superboard-ii-cassette-audio.html

Installation Notes
-------------------
The kcs_encode.py and kcs_decode.py are standalone programs that
should work with any Python 3 installation (version 3.1.2 or newer).
If you decide to install the scripts, they are simply placed
in the Python scripts directory.

Feedback
--------
This is just a fun personal project for me. If you use these scripts
for a vintage computing project, send me email (dave@dabeaz.com) and
let me know about it.  --Dave







This package provides a pair of scripts, kcs_encode.py and kcs_decode.py that encode and decode WAV audio files containing data encoded in the Kansas City Standard as used on some of the first home computers. In my case, an Ohio Scientific Superboard II from 1978. For more information on KCS encoding, see http://en.wikipedia.org/wiki/Kansas_City_standard.

Usage

First of all, you need to install Python-3.1.2 or newer on your system.

To encode a text file into a WAV file suitable for playback, do this:

% python3 kcs_encode.py input.txt output.wav
This reads the file 'input.txt' and writes a WAV file 'output.wav'. The resulting WAV file is encoded in mono with a framerate of 9600 Hz.

To decode a WAV file containing KCS data that you have recorded, do this:

% python3 kcs_decode.py input.wav
Decoded text contained in the WAV file will be printed to standard output. This decoding process will strip NULL bytes and convert line endings to the native line endings for your platform.

If you want to decode raw binary data, type this:

% python3 kcs_decode.py -b input.wav
In this case, output is still directed to standard output, but is exactly as found in the audio (including all NULL bytes).

More Information

See the following blog posts for more information:

http://dabeaz.blogspot.com/2010/08/using-python-to-encode-cassette.html
http://dabeaz.blogspot.com/2010/08/decoding-superboard-ii-cassette-audio.html
Feedback

This is just a fun personal project for me. If you use these scripts for a vintage computing project, send me email (dave@dabeaz.com) and let me know about it. --Dave  (http://www.dabeaz.com/py-kcs/index.html0)

