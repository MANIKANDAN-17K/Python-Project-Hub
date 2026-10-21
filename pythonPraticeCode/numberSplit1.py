while(True):
	num = input("enter value for n and for terminate type exit")
	match num:
		case "exit":
			print("bye")
			break
		case "0":
			print("zero")
		case "1":
			print("positive")
		case "-1":
			print("negative")
		case _:
			print("enter 1,0,1 and exit")
