# cgt
 A modern audiogame creation suite
## Introduction
Several years ago, Blastbay Studios released a program for the creation of AudioGames known as Blastbay Game Toolkit.
The engine was well received, but was unfortunately abandoned, as Blastbay Studios moved onto other things and no longer wished to maintain bgt.
However, game programmers, unwilling to adapt, continued to use the program extensively for as long as they could.
Unfortunately, all good things must come to an end, and as the number of issues with bgt programs grows and game developers reach the software's limits, something had to be done.
This is where the new revolution of audiogames begins: cgt has come in to take the program's place.
Cgt, unofficialy dubbed "chaos game toolkit" by it's developers, is a modern, open source audiogame engine, written in python but with a lua scripting engine.
We chose lua because it is very simple: before cgt, I did not know any lua, and within a day I had learned it completely. It is an extremely simple scripting language and is a great starting point for new programmers. It is similar in some ways to languages such as python.
##examples
Here are some examples of cgt's usage.
###hello world program
speak("Hello world! What is your name?")
name=input()
speak("Nice to meet you, "+name+". My name is chaos!")
speak("Press enter to exit")
input()
