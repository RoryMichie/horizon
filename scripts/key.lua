require "os"
h=0
cs=sound3d("click.wav")
a=newwindow("thing")
while true do
    e=elapsed()
    a.loop()
    if a.held("b")~=h then
        h=a.held("b")
        cs.seek(0)
        cs.play()
        speak(tostring(a.held("b")))
    end
    if a.pressed("h")==1 then
        speak("hello there, you just pressed h")
    end
   f=elapsed()-e
    if f>40 then
        speak(tostring(f))
    end
    if a.pressed("escape")==1 then
        a.close()
    os.exit()
end
    speak(tostring(elapsed()-e))
end
