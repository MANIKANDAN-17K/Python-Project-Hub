class Account:
	def __init__(self):
		self.__balance = 0
		self.a = 10
	def credit(self,amt:int):
		if(amt < 0):
			print("enter positive number")
		self.__balance += amt
	@property
	def check(self)->int:
		return self.__balance;

acc = Account()
acc.credit(10000)
bal =acc.check
print(bal)
print(acc.a)
acc.a = 200
print(acc.a)
acc.balance = 5000
print(acc.check)
