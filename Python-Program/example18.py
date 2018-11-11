import turtle 

name=turtle.textinput("name","What is your name:")
name=name.lower()
if name.startswith("mr"):
	print ("Hello sir" +name+" how are you?")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
	print("Hello Madam, how are you?")
else:
	name=name.capitalize()
	str="hi"+name+"!how are you?"
	print(str)
turtle.exitonclick()
