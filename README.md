# Heathkit ET-3400 Microprocessor Trainer

This repository contains resources for the Heathkit ET-3400 Microprocessor Training System.  We did not generate these resources unless otherwise noted.  These resources are provided to help students gain a deeper understanding of embedded systems.

There are three great resources for emulation that exist.  The required ROM files are present in this repository to run the emulation systems, but are not our creation.  

1) MAME (version 0.193b and later): http://mamedev.org/release.html

2) C Sharp 6800 Emulator: https://sharp6800.codeplex.com/ (Rupert Avery: https://www.codeplex.com/site/users/view/RupertAvery)

3) HyperVision 6800 IDE Assembler: http://www.hvrsoftware.com/6800emu.htm

For MAME, use the debugger in use with the following execution switches (for MAME located in C:\EMULATORS\MAME\) C:\EMULATORS\MAME\mame64.exe -window -debug to allow the debugger to be used (to see the memory locations and use the cassette interface)

Please see the manual excerpt here:  https://archive.org/details/HeathkitManualForTheEt-3400MicroprocessorTrainer and here: http://www.classiccmp.org/dunfield/heath/index.htm, and details on the ET-3400 main board: http://gc.org/et-3400/

Details for the ETA-3400 I/O Accessory: http://www.andysarcade.net/personal/tech/ETA-3400.htm and http://www.vintagecomputer.net/browse_thread.cfm?id=553


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

Motorola 6800 Architecture Overview:  http://www.cpu-world.com/Arch/6800.html

Motorola 6800 Basic Operation Overview:http://www.hvrsoftware.com/6800.pdf

Motolola 6800 Assembly:  http://www.inf.pucrs.br/~calazans/undergrad/orgcomp_EC/mat_microproc/MC6800-AssemblyLProg.pdf

A gret review on the history of modern CPUs: https://www.cl.cam.ac.uk/teaching/2006/CompArch/documents/all/trends/cpu_history.html (The 6800 Family: https://www.cl.cam.ac.uk/teaching/2006/CompArch/documents/all/trends/cpu_history.html#6809)
