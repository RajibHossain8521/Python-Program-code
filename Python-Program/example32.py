# here we work about random number 
#its a one kind of game
import random
number=random.randint(1,1000)
attempts=0

while True:
	input_number=input("Guess the number(between 1 to 1000):")
	input_number=int(input_number)
 	#attempts =attempts + 1
	
	if input_number==number:
		print("Yes, your guess is correct!")
		break
	if input_number>number:
		print("Incorrect!please try to guess a smaller number")
	else:
		print("Incorrect!please try to guess a large number")
print("You tried",attemps,"times to find the correct number.")
