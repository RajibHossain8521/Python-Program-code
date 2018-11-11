# here i make a function for drawing a circle

import turtle
turtle.shape("triangle")
#turtle.speed(1)
turtle.color("blue")

def draw_square(side_length):
	for i in range(4):
		turtle.forward(side_length)
		turtle.left(90)

counter=0
while counter<90:
	draw_square(100) # here i call the function draw_square
	turtle.right(4)
	counter+=1
