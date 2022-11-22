
chaos.Initialize("keyboard test")
speak("initialised")
chaos.TrackKey("a")
chaos.TrackKey("space")
chaos.TrackKey("escape")
speak("tracked keys")
while true do
	chaos.GetCurrentFrameEvents()
	if chaos.KeyPressed("space")==1 then
		speak("beep")
	end
	if chaos.KeyPressed("a")==1 then
		speak("A is for apple.")
	end
	if chaos.KeyPressed("escape")==1 then
		speak("Goodbye")
		chaos.shutdown()
		break
	end
end
