with open("file2.txt","w") as file:
	line1 = file.writelines("apple\n")
	line2 = file.writelines("orange\n")
	line3 = file.writelines("banana")
	print(f"line counts \n line 1 - {line1}\nline2 - {line2}\nline3 - {line3}")

