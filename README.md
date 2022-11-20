# Horizon
			A modern audiogame creation suite
			Version: 0.2.1
## Introduction
Several years ago, Blastbay Studios released a program for the creation of AudioGames known as Blastbay Game Toolkit.

The engine was well received, but was unfortunately abandoned, as Blastbay Studios moved onto other things and no longer wished to maintain bgt.

However, game programmers, unwilling to adapt, continued to use the program extensively for as long as they could.

Unfortunately, all good things must come to an end, and as the number of issues with bgt programs grows and game developers reach the software's limits, something had to be done.

This is where this program comes in.

Horizon is a modern, open source audiogame engine, written in python but with a lua scripting engine. It packs together some of our own components, as well as well loved sound and speech libraries, such as CyTolk, SoundLib, and Synthizer, in such a way that the engine is as easy to use, or as flexible, as you would like it to be.

Programs written in Horizon are actually lua. The engine supports execution within execution to an unlimited number of times: luaexec("luaexec('luaexec(exit())')") is a valid line of code in this engine. The program also supports interaction with the external python environment via the pyeval and pyexec functions

We chose lua because it is very simple: A new programmer can learn it within a week. The language is similar to dynamic languages such as python, so if you wish to change from Horizon into a lower level system, you will have an easier time of it, though we hope that it will provide all the features you need.
## features

The game engine includes features such as:

*3d sound with synthizer

*normal sound with bass

*speech output with tolk

*Event-based keyboard handling with ChaosLib

## examples
Some example scripts are located in the scripts directory.
## dependencies
This engine requires the microsoft visual c++ 2017 redistributeable to work correctly. You can download it from the link below

https://aka.ms/vs/17/release/vc_redist.x64.exe

Although the engine also requires ChaosLib, we have included a binary of it here for simplicity. The source code to this library is not available.

## important note

Horizon is not a finnished product at the time of this writing. We are publishing the code so that those who wish to work on it and track it's development can contribute, learn how it works and experiment, though we do not and will not guarantee it's stability in the foreseeable future.
## Where to get a binary?

Binaries are available for the latest version of Horizon at the link below. 

https://sightlesswolf.com/Horizon0.2.1.zip

