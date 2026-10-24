my_dict = {}
def addValue(key,value):
	my_dict[key] = value

def updateValue(key,value):
	if key in my_dict:
		my_dict[key] = value
	else:
		print(f"given {key} is not founded , enter valid key")
def deleteKey(key):
	if key in my_dict:
		del my_dict[key]
	else:
		print(f"key is not found")
while(True):
	print("Enter any one option \n 1) add key and value \n 2) update value \n 3)remove key \n 4) display \n 5)exit \n ")
	opt = int(input("Enter the option : "))
	if opt == 1:
		key = int(input("Enter key : "))
		value = int(input("Enter Value : "))
		addValue(key,value)
	elif opt == 2:
		key = int(input("Enter existing key : "))
		value = int(input("Enter new Value : "))
		updateValue(key,value)
	elif opt == 3:
		key = int(input("Enter key : "))
		deleteKey(key)
	elif opt == 4:
		print(my_dict)
	elif opt == 5:
		print("bye")
		break
	else:
		print("Enter valid option")

