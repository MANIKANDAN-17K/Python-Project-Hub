class Calculator:
	def add(self,a:int,b:int) -> int:
		return a + b
	def diff(self,a:int,b:int) -> int:
		return a-b
	def mul(self,a:int,b:int) -> int:
		return a * b
	def div(self,a:int,b:int) -> int:
		if b < 1:
			return -1
		return a / b
cal = Calculator()
a = int(input("Enter value of a "))
b = int(input("Enter value of b "))
print(f"add is {cal.add(a,b)}")
print(f"sub is {cal.diff(a,b)}")
print(f"mul is {cal.mul(a,b)}")
print(f"div is {cal.div(a,b)}")
