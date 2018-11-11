# here in this program we again use break and continue logical structure

terminated_program= False
while not terminated_program:
	number1=int(input("please enter a number:"))
	number2=int(input("please enter a another number:"))
	while True:
		operation=input("please enter add/sub or quit to exit:")
		if operation=="quit":
			terminated_program=True
			break
		if operation not in ["add","sub"]:
			print("Unknown operation!")
			continue
		if operation =="add":
			print("Result is",number1+number2)
			break
		if operation=="sub":
			print("Result is",number1-number2)
			break

