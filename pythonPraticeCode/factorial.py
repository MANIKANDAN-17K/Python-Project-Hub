def fact(n:int):
	if(n == 0 or n == 1):
		return 1
	return n * fact(n-1)
n = int(input("Enter value for n : "))
print(f"Factorial of {n} is {fact(n)} .")
