# ET-3400

This repository contains resources for the Heathkit ET-3400 Microprocessor Training System.  We did not generate these resources unless otherwise noted.  

http://mamedev.org/release.html

https://sharp6800.codeplex.com/ (Rupert Avery: https://www.codeplex.com/site/users/view/RupertAvery)

Use the debubber in use with the following execution switches (for MAME located in C:\EMULATORS\MAME\) C:\EMULATORS\MAME\mame64.exe -window -debug to allow the debugger to be used (to see the memory locations and use the cassette interface)

Please see the manual excerpt here:  https://archive.org/details/HeathkitManualForTheEt-3400MicroprocessorTrainer and here: http://www.classiccmp.org/dunfield/heath/index.htm


The kit had the following features:

Motorola 6800 8-bit CPU clocked at 1MHz, Six 7-segment LED displays used to display address and data information, and as a visual output device, 17 push-button switches for the hex keypad, 8 LEDs for general purpose visual output, an 8-bit DIP switch for data input, a 1 KB ROM containing the Monitor program, 256 bytes RAM, buffered 8-bit data and 16-bit address lines, exposed through breadboard connectors.



***************************************************

Quick ET-3400 Guide:

ACCA - View contents of Accumulator A Register

ACCB - View contents of Accumulator B Register

PC - View contents of Program Counter Register

INDEX - View contents of Index Pointer Register

CC - View contents of Condition Codes Register

SP - View contents of Stack Pointer Register

RTI - Return from Interrupt

SS - Single Step

BR - Break

AUTO - Start entering hex at specified address

BACK - During EXAMine mode, move address back

CHAN - During EXAMine mode, edit hex at specified address. During ACCA/ACCB/PC mode, edit hex in selected register

DO - Execute RAM at given address

EXAM - Start viewing hex at specified address

FWD - During EXAMine mode, move address forward

***************************************************
