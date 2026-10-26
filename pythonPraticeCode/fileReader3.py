with open("demo.txt","r") as file:
	line1 = file.readline()
	line2 = file.readline()
	remaining = file.readlines()
	print(f"line 1 is : {line1}")
	print(f"line 2 is : {line2}")
	print(f"remaining is :{remaining}")

