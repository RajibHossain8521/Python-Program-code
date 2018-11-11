import turtle
turtle.shape("triangle")
turtle.color("red")
turtle.speed(5)
counter=0
while counter<36:
	for i in range(4):
		turtle.forward(100)#its a for statement
		turtle.right(90)#its a also for statement
	turtle.right(10) #its a while statement
	counter+=1
turtle.exitonclick()
