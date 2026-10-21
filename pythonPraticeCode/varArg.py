def totSum(*arg):
	tot = 0
	for i in arg:
		tot += i
	return tot
print(f" total sum of 3, 5, 9, 4 is {totSum(3,5,9,4)}")
