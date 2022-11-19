
chaos.Initialize("keyboard test")
speak("initialised")
chaos.TrackKey("a")
chaos.TrackKey("space")
speak("tracked keys")
while true do
	chaos.GetCurrentFrameEvents()
	repeat
		chaos.NextFrameEvent()
		e=chaos.EventInfo()
		if e==event_key_push then
			speak("beep")
			v=keyname(chaos.EventValue())
			speak(v)
			if v=="space" then
				speak("Space pressed.")
			end
			if v=="a" then
				speak("a is for apple")
			end
		end
	until e==event_none
end
