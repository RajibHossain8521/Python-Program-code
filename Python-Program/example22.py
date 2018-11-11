# here we use break and continue logical structure

while True:
	n=int(input("please enter possitive number(0 to exit:):"))
	if n<0:
		print("we can only allow possitive number.please try again")

		continue
	if n==0:
		break
	print("Square of",n,"is",n*n)
