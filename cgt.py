import math
from sound_lib import output,stream
import random
from cytolk import tolk
import time
tolk.load()
f=None
import lupa
a=lupa.LuaRuntime()
b=input("Enter a file to run lua code from it")
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
def runcode():
    o=output.Output()
    addfunc("sine",math.sin)
    addfunc("cosine",math.cos)
    addfunc("tangent",math.tan)
    addfunc("arc_sine",math.asin)
    addfunc("arc_cosine",math.acos)
    addfunc("arc_tangent",math.atan)
    addfunc("pi",math.pi)
    addfunc("radians_to_degrees",math.degrees)
    addfunc("degrees_to_radians",math.radians)
    addfunc("luaexec",luaexec)
    addfunc("pyexec",exec)
    addfunc("luaeval",a.eval)
    addfunc("urlsound",urlsound)
    addfunc("pyeval",eval)
    addfunc("sound",sound)
    addfunc("elapsed",time.time)
    addfunc("random",random.randint)
    addfunc("random_seed",random.seed)
    addfunc("wait",wait)
    addfunc("speak",tolk.speak)
    addfunc("input",input)
    try:
        a.execute(f.read())
    except Exception as e:
        tolk.speak("An error occured: "+str(e)+". Press enter to continue")
        input()

f=open(b,"rb")
runcode()
