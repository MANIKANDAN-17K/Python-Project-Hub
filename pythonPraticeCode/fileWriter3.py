text = ["hi this is mani \n","welcome to  goML \n","i am intern at goML"]
with open("file3.txt","w") as file:
	file.writelines(text)
	print("file wrote successfully")

