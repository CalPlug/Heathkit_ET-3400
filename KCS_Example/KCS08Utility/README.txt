This is an alternative way of Reading and Writing KCS Audio to and from files

This program must be run in DOSBOX (Tested on v0.74) on the Windows 10 PC on which it was tested.

This is provided as an alternative approach.  We did not modify the contents of this software.  All credit for development goes to the original authors.

Please see this article for use:  http://www.instructables.com/id/Storing-files-on-an-audio-cassette/
The original KCS08 software is hosted here:  ftp://ftp.taygeta.com/pub/forth/compilers/native/dos/DXForth/kcs08.txt

Usage:
1)  A smiley face image is provided for testing.  Place the KCS08 files and this image in a directory that can be mounted by DOSBOX
2) Encode with this sample command:  KCS -M -Y -U -L5 SMILEY.JPG OUTPUT.WAV  (see:  http://www.instructables.com/id/Storing-files-on-an-audio-cassette/)
3) Record to Tape using Audacity (not in DOSBOX, obviously!)
4) Record From tape using Audacity (not in DOSBOX, obviously!)
5) Decode with this sample command:  KCS -Y -U  OUTPUT.WAV SMILEY_D.JPG
