a=newwindow("thing")
while true do
    a.loop()
    if a.released("h")==1 then
        speak("hello there, you just pressed h")
    end
end
