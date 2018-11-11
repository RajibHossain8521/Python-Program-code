# here we see what is a local variable
# and what is a Global variable

def  myfunction(x): # in this line "x" is a Perameter of myfunction
	print("inside myfunction",x)
	x=10 # here x=10 is local variable 
	     # beacuse the variable which is declare in the function they called local variable
	print("inside myfunction",x)
x=20    #this is global variable ,because the variable which declare outside of the function they called global variable
myfunction(x)
print(x)
	
