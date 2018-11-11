#this program find the circle area
#here we import math module
import math
radius=input("please enter your radius value:")
radius=float(radius)
circle_area=math.pi*radius*radius #math module atumatically declare the pi value but if we don't use math module so before use pi we need declare the pi number
print("Area of circle:{:.2f}".format(circle_area))
