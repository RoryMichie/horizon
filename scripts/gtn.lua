require "io"
require "math"
target=math.random(1,100)
io.write("Welcome to guess the number. Let's see if you can find my number, between 1 and 100")
while true do
	io.write("Enter your guess\n")
	g=tonumber(io.read())
	if g<target then
	io.write("Too low!\n")
	elseif g>target then
		io.write("Too high!\n")
	else
		io.write("Yay, you win!\n")
		wait(1)
		break
	end
end
