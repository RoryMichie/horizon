target=random(1,100)
speak("Welcome to guess the number. Let's see if you can find my number, between 1 and 100")
while true do
	speak("Enter your guess")
	g=tonumber(input())
	if g<target then
	speak("Too low!")
	elseif g>target then
		speak("Too high!")
	else
		speak("Yay, you win!")
		wait(1)
		break
	end
end
