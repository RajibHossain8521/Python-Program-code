#this program also find out that the year is a leap year or not
#here this program use "and " keywords 
year=input ("please type an integer value:")
year=int(year)
if year%100 !=0 and year%4==0:
	print("this",year,"is a leap year")
elif year%100==0 and year%400==0:
	print ("this ",year,"is a leap year")
else:
	print("this ",year,"is not a leap year")

