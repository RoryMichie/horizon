import keys
import sdl2
import sdl2.ext
sdl2.ext.init()
h=0
a=keys.newwindow("ball")
while True:
	a.loop()
	if h!=a.held("b"):
		h=a.held("b")
