#find the average of n series ,after will be write accurately
import sys #what is sys in pyhton?
n=input("Enter a positive integer number:")

n=int(n) #it's means 'n' always take integer number
if n==0:
	sys.exit(1) #if the value of n ==0 then it go out from system

sum=0
for i in range (n): #what the number take from user and the value of i in range of n then it go for next step

	i=input("Enter a number:") #its take the number according of 'n' number
	i=float(i)
	sum=sum+i
average = sum/n
print("The average is:{:.2f}",average) #{:.2f} means of f =float and (.2)=it's show the first two digits of   						float number after the dot(.)
	
