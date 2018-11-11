# in this program we find the result from celsius to fahrenhite

celsius=input("enter the temparature of celsius:")
celsius=float(celsius)

farhenhite=celsius*1.8+32

#if we want take two digit after point then use round() function

farhenhite=round(farhenhite,2)
print("temparature in farhenhite is:",farhenhite)

#here we find the result from farhenhite to celsius
farhenhite=input("enter the temparature of farhenhite:")
farhenhite=float(farhenhite)

celsius=(farhenhite-32)/1.8
celsius=round(celsius,2)
print("temparature of celsius is:",celsius)


