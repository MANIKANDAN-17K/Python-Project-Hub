class Animal:
	def sound(self):
		print("Animal make sound")
	def eat(self):
		print("Animal eat food")
class Dog(Animal):	
	def sound(self):
		print("dog make bow,bow ! sound")
	def eat(self):
		print("dog eat piece of bone")
class Cat(Animal):
	def sound(self):
		print("cat make meo, meo ! sount")
	def eat(self):
		print("cat eat fish")
class Crocodile(Animal):
	pass

dog = Dog()
cat = Cat()
cc = Crocodile()
dog.sound()
dog.eat()
cat.sound()
cat.eat()
cc.sound()
cc.eat()
