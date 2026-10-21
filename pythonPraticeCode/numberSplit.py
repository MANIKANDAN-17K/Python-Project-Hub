while(True):
	num = int(input("Enter value for n and exit -1 "))
	if num == -1:
		print("negative number")
		print("bye")
		break
	elif num == 0:	
		print("number is zero")
	elif num > 0:
		print(" positive number ")
	else: 
		print(" negative number ")

