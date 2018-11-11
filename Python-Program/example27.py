def add_numbers(numbers):
	result=0
	for number in numbers:
		result+=number
		average=result/2
	return average
result=add_numbers([1,2,3,4])
print(result)
