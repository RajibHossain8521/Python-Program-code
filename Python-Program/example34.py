# this program find the 'Prime Number' using defferent type of methods

#function1 for Prime number
"""def is_prime1(n):
	if n<2:
		return False
	prime=True
	for x in range(2,n):
		if n % x == 0:
			print(n,"is divided by",x)
			prime = False #this line show the else statement
	return prime
while True:
	number=input("Please enter a positive number(0 to exit):")
	number=int(number)
	if number == 0:
		break
	prime = is_prime1(number)
	if prime is True:
		print(number,"is a prime number")
	else:
		print(number,"is not a prime number")""" 

#function2 for Prime number
"""def is_prime2(n):
	if n<2:
		return False
	prime=True
	for x in range(2,n):
		if n % x == 0:
			print(n,"is divided by",x)
			prime = False
			break
	return prime
while True:
	number=input("Please enter a positive number(0 to exit):")
	number=int(number)
	if number == 0 :
		break
	prime=is_prime2(number)
	if prime is True:
		print(number,"is a prime number")
	else:
		print(number,"is not a prime number")"""

#function3 for Prime number
def is_prime3(n):
	if n == 2:
		return True # 2 is prime number 
	if n % 2 == 0:
		print(n,"is divided by 2")
	return False # all even numbers except 2 are not prime
	if n<2:
		return False # numbers less than 2 are not prime
	prime= True
	for x in range(3,n,2):
		if n % x == 0:
			print(n,"is divided by",x)
			prime= False
			break
	return prime
while True:
	number=input("Please enter a positive number(0 to exit):")
	number=int(number)
	if number == 0:
		break
	prime=is_prime3(number)
	if prime is True:
		print(number,"is a prime number")
	else:
		print(number,"is not a prime number")

"""#loop modify statement
m= n // 2 + 1
for x in range(3,m,2):

#function4 for Prime number

import math

def is_prime4(n):
	if n<2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	m = math.sqrt(n)
	m = int(m) + 1
	for x in range(3,m,2)
		if n % x == 0:
			return False
	return True"""


		

