import ctypes
from sound_lib import output,stream
import random
from cytolk import tolk
import time
tolk.load()
f=None
import lupa
a=lupa.LuaRuntime()
def addfunc(shit,shit2):
    a.globals()[shit]=shit2
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
    a.execute(code)
def init():
    o=output.Output()
    addfunc("luaexec",luaexec)
    addfunc("pyexec",exec)
    addfunc("luaeval",a.eval)
    addfunc("urlsound",urlsound)
    addfunc("pyeval",eval)
    addfunc("sound",sound)
    addfunc("elapsed",time.time)
    addfunc("wait",wait)
    addfunc("speak",tolk.speak)
def runcode(b):
    try:
        a.execute(b)
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
