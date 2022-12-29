import lupa
class F:
	def test(self):
		return "hi"
runtime = lupa.LuaRuntime()
data='''
f=F()
while true do
f.test()
end'''
runtime.globals()['F'] = F
runtime.execute(data)

