import ctypes
from sound_lib import output,stream
import random
from cytolk import tolk
import time
tolk.load()
f=None
import lupa
CGTRuntime=lupa.LuaRuntime()
def addfunc(name,ref):
    CGTRuntime.globals()[name]=ref
def urlsound(urlname):
    handle=stream.URLStream(url=urlname)
    return handle
def sound(filename):
    handle=stream.FileStream(file=filename)
    return handle
def wait(j):
    t=time.time()
    while True:
        if time.time()>=t+j:
            return
def luaexec(code):
    CGTRuntime.execute(code)
def init():
    o=output.Output()
    addfunc("luaexec",luaexec)
    addfunc("pyexec",exec)
    addfunc("luaeval",CGTRuntime.eval)
    addfunc("urlsound",urlsound)
    addfunc("pyeval",eval)
    addfunc("sound",sound)
    addfunc("elapsed",time.time)
    addfunc("wait",wait)
    addfunc("speak",tolk.speak)
def runcode(b):
    try:
        CGTRuntime.execute(b)
    except Exception as e:
        print("An error occured: "+str(e)+". Press enter to continue")
        input()
init()
def console():
    print("Welcome to the cgt debugging console.")
    while True:
        print(">>>")
        runcode(input())
while True:
    print("Select something to do: run, or console",end="\r\n")
    s=input()
    if s=="run":
        b=input("Enter a file to run lua code from it")
        f=open(b)
        runcode(f.read())
    if s=="console":
        console()
