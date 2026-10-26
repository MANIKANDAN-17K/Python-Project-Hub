def greet():
	print("hello, world!")
def exe_fun(a,b,callback):
	print(a+b)
	callback()
exe_fun(90,53,greet)

