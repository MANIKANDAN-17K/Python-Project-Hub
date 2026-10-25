from abc import ABC,abstractmethod 
class Payment(ABC):
	@abstractmethod
	def pay(self,amt:float):
		pass
class CasePayment(Payment):
	def pay(self,amt:float):
		print(f"you paid {amt} amount via liquid case ")
class UPIPayment(Payment):
	def pay(self,amt:float):
		print(f"you paid {amt} amount via  UPIPayment ")
case = CasePayment()
case.pay(2000)
upi = UPIPayment()
upi.pay(500)
