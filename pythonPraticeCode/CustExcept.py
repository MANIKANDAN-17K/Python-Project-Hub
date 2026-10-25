class InsufficientBalance(Exception):
	pass
def debit(balance, amount):
	if(balance < amount):
		raise InsufficientBalance("you bank balance in sufficient")
	print(f"amount {amount} is debit and balance is {balance - amount}")
try:
	balance = 100
	amt = int(input("Enter you amount"))
	debit(balance,amt)
except InsufficientBalance as error:
	print(error)
