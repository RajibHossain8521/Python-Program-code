#this program find the triangle area by using a function
import math
def calculate_area(a,b,c):
	#check if such triangle possible
	if (a+b)>c and (b+c)>a and (a+c)>b:
		s=(a+b+c)/2
		area=math.sqrt(s*(s-a)*(s-b)*(s-c))
		return area
	else:
		#not possible to form a triangle
		#with these sides
		return None
data=input("Enter the three sides of triangle:")
#if you use split() function for collecting the input value 
#then you no need to write more line for taking input value
a,b,c=data.split()
a=float(a)
b=float(b)
c=float(c)
area=calculate_area(a,b,c)

if area is not None:
	print("triangle area:{:.2f}".format(area))
else:
	print("it is not possible to form a triangle with thses sides")
