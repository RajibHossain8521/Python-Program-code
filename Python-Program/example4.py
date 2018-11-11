#find the smallest value among three values
#here each number compare with other number 
#and show the smallest number
num1=input ("please type an integer number:")
num2=input ("please type an integer number:")
num3=input ("please type an integer number:")
num1=int (num1)
num2=int (num2)
num3=int (num3)
if num1<num2 and num1<num3:
	print(num1,"is smallest")
elif num2<num3 and num2<num1:
	print(num2,"is smallest")

else:
	print(num3,"is smallest")
