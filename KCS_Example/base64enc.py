#!/usr/bin/env python3
# base64conv.py
#
# A simple utility to base 64 encode files provided
#
# Author : Michael Klopfer
# Copyright (C) 2017
#
# Requires Python 3.1.2 or newer

import base64

if __name__ == '__main__':
	import sys
	if len(sys.argv) != 3:
		print("Usage : %s infile outfile" % sys.argv[0],file=sys.stderr)
		raise SystemExit(1)

	in_filename = sys.argv[1]
	out_filename = sys.argv[2]
	data = open(in_filename,"rb").read()
	b64_encode = base64.encodestring(data)
	file_output = open(out_filename, 'wb') # create a writable image and write the decoding result
	file_output.write(b64_encode)
	file_output.close()

	
    
