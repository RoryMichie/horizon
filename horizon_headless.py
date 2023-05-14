import argparse
import gc
import os
import sys
import time

sys.coinit_flags = 0
import lupa

horizon_version = "0.4.0 alpha"
horizon_runtime = lupa.LuaRuntime()


def lua_wrap(name, ref):
    horizon_runtime.globals()[name] = ref


def lua_exec(code):
    horizon_runtime.execute(code)


def init():

    lua_wrap("changedir", os.chdir)
    lua_wrap("len", len)
    lua_wrap("collect_garbage", gc.collect)
    lua_wrap("luaexec", lua_exec)
    lua_wrap("pyexec", exec)
    lua_wrap("luaeval", horizon_runtime.eval)
    lua_wrap("pyeval", eval)
    lua_wrap("elapsed", time.time)
    lua_wrap("wait", time.sleep)
    parse_command()


def runcode(b):
    horizon_runtime.execute(b)


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
    group.add_argument(
        "-v",
        "--version",
        help="Displays horizon version, as well as lua version and implementation.",
        action="store_true",
    )
    args = parser.parse_args()
    if args.console:
        console()
    elif args.version:
        print(
            "Horizon version: "
            + horizon_version
            + ". "
            + horizon_runtime.lua_implementation
            + " (lua version "
            + str(horizon_runtime.lua_version)
            + ")."
        )
    elif args.filename is not None:
        with open(args.filename) as f:
            runcode(f.read())
    if len(sys.argv) == 1:
        parser.print_help()


if __name__ == "__main__":
    init()
