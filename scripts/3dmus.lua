a=newwindow("3d music player")
s=sound3d("music.wav")
s.play()
x=0
y=0
z=0
timer=elapsed()
looping = false
while true do
a.loop()
addx=0
addy=0
addz=0
if elapsed()-timer>0.099 then
if a.held("left")==1 then
addx=addx-1
end
if a.held("right")==1 then
addx=addx+1
end
if a.held("down")==1 then
addy=addy-1
end
if a.held("up")==1 then
addy=addy+1
end
if a.held("pagedown")==1 then
addz=addz-1
end
if a.held("pageup")==1 then
addz=addz+1
end
if a.pressed("c")==1 then
x = 0
y = 0
z = 0
addx = 0
addy = 0
addz = 0
s.position(x,y,z)
end
if a.pressed("l")==1 then
if looping == false then
looping = true
else
looping = false
end
s.loop(looping)
end
if addx~=0 or addy~=0 or addz~=0 then
x=x+addx
y=y+addy
z=z+addz
s.position(x,y,z)
timer=elapsed()
end
end
if a.pressed("escape")==1 then
a.close()
end
end
