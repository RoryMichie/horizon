function runmenu(w,mlist)
clicksound=sound("menuclick.wav")
entersound=sound("menuenter.wav")
entersound.volume=0.3
clicksound.volume=0.3
pos=0
while true do
w.loop()
if w.pressed("down")==1 and pos<len(mlist) then
pos=pos+1
clicksound.set_position(0)
clicksound.play()
speak(mlist[pos])
end
if w.pressed("up")==1 and pos>1 then
pos=pos-1
clicksound.set_position(0)
clicksound.play()
speak(mlist[pos])
end
if w.pressed("enter") ==1 then
entersound.play()
return pos
end
end
end
