# here i code for function

def function(x,z,y=10): #if i declare the defult value of any perameter 
                         # then after all perameter value must will be a default value

	print("x=",x,"y=",y,"z=",z)

function(x=1,y=2,z=3) #here i send the value for perameter as i want
a=5
b=6
function(x=a,z=b)
a=3
b=4
c=6
function(y=a,x=b,z=c)
a=10
function(x=a)


