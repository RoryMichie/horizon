# Horizon
            A modern audiogame creation suite
## Introduction
Horizon is a modern, open source audiogame engine, written in python but with a lua scripting engine. It packs together some of our own components, as well as well-loved sound and speech libraries, such as Accessible Output 2, SoundLib, and Synthizer, in such a way that the engine is as easy to use, or as flexible, as you  need  it to be.
We chose lua because it is very simple: A new programmer can learn it within a week. The language is similar to dynamic languages such as python, so if you wish to change from Horizon into a lower-level system, you will have an easier time of it, though we hope that it will provide all the features you need.
Horizon also provides modularity, with many of its functions being directly usable without incorperating  Lua into your projects.
This includes, but is not limited to, Horizon's keyboard wrapper, both sound wrappers, and utility functions all being usable in a pure Python execution environment.
## features

The game engine includes features such as:

* 3d sound with synthizer

* Mono and stereo sound with bass

* Speech output with AO2

* Event-based keyboard handling with SDL2

## examples
Some example scripts  can be found in the script’s directory.
## dependencies
This engine requires the Microsoft visual c++ 2017 redistributable to work correctly on Windows. You can download it from the link below

https://aka.ms/vs/17/release/vc_redist.x64.exe


## Important note

Horizon is not a finished product at the time of this writing. We are publishing the code so that those who wish to work on it and track its development can contribute, learn how it works and experiment, though we do not and will not guarantee its stability soon.
## Platform support
Horizon should work out of the box on the following platforms:
* Windows
    * X64
    * ARM64
* Linux
    * X86-64
    * ARM64
### A brief note about Mac OS
It has come to our attention that there is a rather nasty bug in the current version of Synthizer that effectively prevents it from being used on MacOS. While the engine itself theoretically supports MacOS, sound is incredibly important for proper game creation and enjoyment. Therefore, MacOS will be treated as unsupported until or unless this bug within the primary sound module is resolved.
## untested platforms
These platforms should work; however, they have not been evaluated and we will not be providing support for issues relating to building and running on said platforms
* X86: aka IA32: this goes for Linux, Mac, and Windows as 32-bit hardware has become obsolete
* ARM32: Hardware is simply unavailable to easily test this architecture, however it should work as expected assuming that compilers and toolchains exist that will compile everything that is required for the engine.
* Mips, PPc, etc.: These architectures are not common among consumer hardware, and thus they have not been tested.

