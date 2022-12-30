# Horizon
            A modern audiogame creation suite
            Version: 0.2.1
## Introduction
Several years ago, Blastbay Studios released a program for the creation of Audio Games known as Blastbay Game Toolkit.

The engine was well received, but was unfortunately abandoned, as Blastbay Studios moved onto other things and no longer wished to maintain bgt.

However, game programmers, unwilling to adapt, continued to use the program extensively for as long as they could.

Unfortunately, all good things must end, and as the number of issues with bgt programs grows and game developers reach the software's limits, something had to be done.

This is where this program comes in.

Horizon is a modern, open source audiogame engine, written in python but with a lua scripting engine. It packs together some of our own components, as well as well-loved sound and speech libraries, such as Accessible Output 2, SoundLib, and Synthizer, in such a way that the engine is as easy to use, or as flexible, as you would like it to be.

Programs written in Horizon are lua. The engine supports execution within execution to an unlimited number of times: luaexec ("luaexec ('luaexec (exit ())')") is a valid line of code in this engine. The program also supports interaction with the external python environment via the pyeval and pyexec functions

We chose lua because it is very simple: A new programmer can learn it within a week. The language is similar to dynamic languages such as python, so if you wish to change from Horizon into a lower-level system, you will have an easier time of it, though we hope that it will provide all the features you need.
## features

The game engine includes features such as:

*3d sound with synthizer

* Mono and stereo sound with bass

*Speech output with AO2

*Event-based keyboard handling with SDL2

## examples
Some example scripts are in the script’s directory.
## dependencies
This engine requires the Microsoft visual c++ 2017 redistributable to work correctly. You can download it from the link below

https://aka.ms/vs/17/release/vc_redist.x64.exe


## Important note

Horizon is not a finished product at the time of this writing. We are publishing the code so that those who wish to work on it and track its development can contribute, learn how it works and experiment, though we do not and will not guarantee its stability soon.
## Platform support
Horizon should work out of the box on the following platforms:
* Windows
    * X64
    * ARM64
* Mac OS
    * X86-64
    * Apple m1/m2(aka ARM64)
* Linux
    * X86-64
    * ARM64

### untested platforms
These platforms should work; however, they have not been evaluated and we will not be providing support for issues relating to building and running on said platforms
* X86: aka IA32: this goes for Linux, Mac, and Windows as 32-bit hardware has become obsolete
* ARM32: Hardware is simply unavailable to easily test this architecture, however it should work as expected with minor tweaks
* Mips, PPc, etc.: These architectures are not common among consumer hardware, and thus they have not been tested.

