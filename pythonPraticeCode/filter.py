List = [2,3,1,4,6]
print(List)
newList = [x for x in List if x % 2 == 0]
print(newList)
squreList = [ x * x for x in newList]
print(squreList)
