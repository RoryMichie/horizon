a=newwindow("thing")
while true do
    e=elapsed()
    a.loop()
    if a.pressed("h")==1 then
        speak("hello there, you just pressed h")
    end
	speak(tostring(elapsed()-e))
end
