import synthizer
from sound_lib import output,stream
import random
from cytolk import tolk
import time
tolk.load()
f=None
import lupa
CGTRuntime=lupa.LuaRuntime()

class sound_synthizer:
    def __init__(self, filename, context):
        self.filename = filename
        self.context = context
        self.context.default_panner_strategy.value = synthizer.PannerStrategy.HRTF
        self.buffer = synthizer.Buffer.from_file(filename)
        self.generator = synthizer.BufferGenerator(context)
        self.generator.buffer.value = self.buffer

        self.source = synthizer.Source3D(context)
        self.source.add_generator(self.generator)
        self.source.pause()
        self.generator.playback_position.value = 0

    def play(self):
        self.source.play()

    def pause(self):
        self.source.pause()

    def position(self, x, y=0, z=0):
        self.source.position.value = (x, y, z)

    def seek(self, position):
        self.generator.playback_position.value = position

    def gain(self, volume):
        gain = 10**(volume/20)
        self.source.gain.value = gain

    def __del__(self):
        self.source.dec_ref()
        self.generator.dec_ref()
        self.buffer.dec_ref()
def addfunc(name,ref):
    CGTRuntime.globals()[name]=ref
def sound3d(name):
    return sound_synthizer(name,ctx)
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
    global ctx
    o=output.Output()
    addfunc("luaexec",luaexec)
    addfunc("pyexec",exec)
    addfunc("luaeval",CGTRuntime.eval)
    addfunc("urlsound",urlsound)
    addfunc("pyeval",eval)
    addfunc("sound",sound)
    addfunc("sound3d",sound3d)
    addfunc("elapsed",time.time)
    addfunc("wait",wait)
    addfunc("speak",tolk.speak)
    with synthizer.initialized(
    log_level=synthizer.LogLevel.DEBUG, logging_backend=synthizer.LoggingBackend.STDERR):
        print("Initialised. Getting context...")
        ctx = synthizer.Context()
        print("Context retrieved. Setting panner strategy.")
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
        print("Select something to do: run, or console",end="\r\n")
        s=input()
        if s=="run":
            b=input("Enter a file to run lua code from it")
            f=open(b)
            runcode(f.read())
        if s=="console":
            console()
init()
