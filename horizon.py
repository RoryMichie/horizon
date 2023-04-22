import argparse
import gc
import os
import sys
import time

sys.coinit_flags = 0
import accessible_output2.outputs.auto
import lupa

import keys
import sound
import sound_synthizer
from sound_synthizer import synthizer


horizon_version="0.4.0 alpha"
horizon_runtime = lupa.LuaRuntime()


def lua_wrap(name, ref):
    horizon_runtime.globals()[name] = ref





def luaexec(code):
    horizon_runtime.execute(code)


def init():
    global ctx
    global ao
    ao = accessible_output2.outputs.auto.Auto()
    lua_wrap("changedir", os.chdir)
    lua_wrap("len", len)
    lua_wrap("collect_garbage", gc.collect)
    lua_wrap("keys", keys)
    lua_wrap("newwindow", keys.newwindow)
    lua_wrap("luaexec", luaexec)
    lua_wrap("pyexec", exec)
    lua_wrap("luaeval", horizon_runtime.eval)
    lua_wrap("urlsound", sound.urlsound)
    lua_wrap("pyeval", eval)
    lua_wrap("sound", sound.sound)
    lua_wrap("sound3d", sound3d)
    lua_wrap("elapsed", time.time)
    lua_wrap("speak", ao.output)  # It does braille too
    lua_wrap("wait", time.sleep)
    with synthizer.initialized():

        ctx = synthizer.Context()


        parse_command()


def sound3d(filename,hrtf=True,source_type="3d"): return sound_synthizer.sound_synthizer(filename,ctx,hrtf,source_type)
def runcode(b):
    # try:
    horizon_runtime.execute(b)


#    except Exception as e:
#        print("An error occured: "+str(e)+". Press enter to continue")

#        input()


def console():
    print("Welcome to the horizon debugging console.")
    while True:
        print(">")
        runcode(input())


def parse_command():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-c",
        "--console",
        help="launch a console for testing and debugging",
        action="store_true",
    )
    group.add_argument("-f", "--filename", help="the name of the file to be executed")
    group.add_argument("-v","--version",help="Displays horizon version, as well as lua version and implementation.",action="store_true")

    args = parser.parse_args()
    if args.console:
        console()
    elif args.version:
        print("Horizon version: "+horizon_version+". "+horizon_runtime.lua_implementation+" (lua version "+str(horizon_runtime.lua_version)+").")
    elif args.filename is not None:
        with open(args.filename) as f:
            runcode(f.read())
    if len(sys.argv) == 1:
        parser.print_help()


def main():
    init()


if __name__ == "__main__":
    main()
