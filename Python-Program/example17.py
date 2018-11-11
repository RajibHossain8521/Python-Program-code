#we also use all methods or function conditionally
#in this program we learn how to use method in conditional program
list=["Bangladesh","swizerland","finland","india","bhutan","nepal"]
print(list)
item=input("please input your string:")
item=str(item)
if item in list:
	print("sorry sir its already exist")
else:
	list.append(item)
print(list)
