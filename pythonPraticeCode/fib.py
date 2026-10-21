a,b = 0,1
def fib(n):
	global a,b
	if(n == 0):
		return
	a,b = b,a+b
	print(a)
	n -= 1
	fib(n)
print(f"0")
fib(5)
