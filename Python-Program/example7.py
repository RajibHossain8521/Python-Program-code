#this program draw a triangle by using  function

import turtle
turtle.speed(1)
arm_length=input("please enter your integer type value:")
arm_length=int(arm_length)
# here i am declare a function for draw triangle

def draw_triangle(arm_length):#here (arm_length) is function perameter 
	turtle.forward(arm_length)# herer (arm_length) is argument
	turtle.left(120)
	turtle.forward(arm_length)
	turtle.left(120)
	turtle.forward(arm_length)
	turtle.left(120)
