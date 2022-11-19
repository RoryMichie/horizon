
chaos.Initialize("keyboard test")
speak("initialised")
chaos.TrackKey("a")
chaos.TrackKey("space")
speak("tracked keys")
while true do
	chaos.GetCurrentFrameEvents()
	repeat
		speak("shit")
		chaos.NextFrameEvent()
		e=chaos.EventInfo()
		if e==event_key_pushed then
			a=sound("music.wav")
			a.play()
v=chaos.KeyValueToString(chaos.EventValue())
			if v=="space" then
				speak("Space pressed.")
			end
			if v=="a" then
				speak("a is for apple")
			end
		end
	until e==event_none
end
