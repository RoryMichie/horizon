
h2=0
a=newwindow("thing")
while true do
    e=elapsed()
    a.loop()
    h=a.held("b")
    if h2~=h then
        h2=h
    end
    if a.pressed("h")==1 then
        speak("hello there, you just pressed h")
    end
end
