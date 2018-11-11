#this program for find out that the year is leap year or not
year=input("please type an integer value: ")
year=int(year)
if year%2 !=0:# if year has any reminder that mean its not a leap year but if year has no any remind then its go for next step.  
	print("this",year," is not a leap year")
else :
	if year%100==0:
		if year%400==0:
			print("this ",year,"is leap year")
		else:
			print("this",year,"is not a leap year")		
	else :
		print("this",year,"is leap year")
