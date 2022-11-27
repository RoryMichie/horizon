require "io"
io.write("welcome to the calculator.\n")
while true do
    io.write("Please, enter an equation\n")
    io.write("The answer is" .. luaeval(io.read()) .. "\n")
end
