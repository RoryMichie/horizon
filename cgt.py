import ctypes
import lupa
import sound_synthizer
from sound_synthizer import synthizer
import sound
import random
from cytolk import tolk
import time
tolk.load()
CGTRuntime = lupa.LuaRuntime()


def addfunc(name, ref):
    CGTRuntime.globals()[name] = ref

def sound3d(name):
    return sound_synthizer.sound_synthizer(name, ctx)

def wait(j):
    t = time.time()
    while True:
        if time.time() >= t+j:
            return


def luaexec(code):
    CGTRuntime.execute(code)


def init():
    global ctx
    chaos=ctypes.cdll.LoadLibrary("./chaos.dll")
    chaos.KeyValueToString.restype=ctypes.c_wchar_p
    addfunc("chaos",chaos)
    addfunc("event_none",-1)
    addfunc("event_key_push",0)
    addfunc("event_key_release",1)
    o = sound.output.Output()
    addfunc("luaexec", luaexec)
    addfunc("pyexec", exec)
    addfunc("luaeval", CGTRuntime.eval)
    addfunc("urlsound", sound.urlsound)
    addfunc("pyeval", eval)
    addfunc("sound", sound.sound)
    addfunc("sound3d", sound3d)
    addfunc("elapsed", time.time)
    addfunc("wait", wait)
    addfunc("speak", tolk.speak)
    with synthizer.initialized(
            log_level=synthizer.LogLevel.DEBUG, logging_backend=synthizer.LoggingBackend.STDERR):

        ctx = synthizer.Context()

        ctx.default_panner_strategy.value = synthizer.PannerStrategy.HRTF
        main()


def runcode(b):
    try:
        CGTRuntime.execute(b)
    except Exception as e:
        print("An error occured: "+str(e)+". Press enter to continue")
        
        input()


def console():
    print("Welcome to the cgt debugging console.")
    while True:
        print(">>>")
        runcode(input())


def main():
    while True:
        print("Select something to do: run, or console", end="\r\n")
        s = input()
        if s == "run":
            b = input("Enter a file to run lua code from it")
            f = open(b)
            runcode(f.read())
        if s == "console":
            console()


init()
