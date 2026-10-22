List = [("mani",22),("ravi",12),("siva",18),("vishal",9)]
List.sort(key=lambda x:x[1])
print(List)
List.sort(key=lambda x:x[1],reverse=True)
print(List)
res = sorted(List,key=lambda x:x[1])
print(res)
print("old list",List)
