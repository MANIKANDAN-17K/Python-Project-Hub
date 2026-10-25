try:
	a = input("Enter value for a ")
	b = int(input("Enter value for b "))
	n3 = int(a)/b
	print(n3)
except ZeroDivisionError:
	print("b should not be zero")
except ValueError as error:
	print(error)
finally:
	print("program executed successfully")

