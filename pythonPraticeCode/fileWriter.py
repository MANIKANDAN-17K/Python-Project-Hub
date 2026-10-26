text = "hello this is form developer mani "
with open("file1.txt","w") as file:
	count = file.write(text)
	print(f"file wrote successfully and its count {count}")

