st = input("Enter the String")

def reverseString(st:str) -> str:
	temp = ""
	lt = list(st)
	n = len(lt)
	for i in range(n-1,-1,-1):
		temp += lt[i]
	return temp
def easyReverse(st:str) -> str:
	return st[::-1]

rev = reverseString(st)
er = easyReverse(st)
print(f"original String is {st} \n reversed String is {rev} \n another method str[::-1] is{er}")


