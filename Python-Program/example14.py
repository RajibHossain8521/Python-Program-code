days=input("enter number of days:")
days=int(days)
month=days // 30
new_days=days % 30

if month ==0:
	print(days,"days=",newa_days,"days")
elif month==1:
	print(days,"days=",month,"month and",new_days,"days")
else:
	print(days,"days=",month,"months and",new_days,"days")
