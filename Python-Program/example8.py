# find the list average by function
#this funtion for find the average of list
def calculate_avg(li):#this function take a list as a perameter
	n=len(li)# here len() function find the length of list
	tottal=0 #here we declare tottal =0
	for x in li:
		tottal=tottal+x
		average =tottal/n
		return average
