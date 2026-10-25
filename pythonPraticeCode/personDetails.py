class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def display(self):
		print(f"Person name is {self.name}")
		print(f"Person age is {self.age}")
name = input("Enter you name")
age = int(input("Enter you age"))
person = Person(name,age)
person.display()
