# in this program we are write program about all kind of python data structure
#first we start with list
saarc=["Bangladesh","finland","india","bhutan","nepal"]
#this line show the list value of saarc
print(saarc) 
#here we use append() method for add new data in list
saarc.append("swizerland")
#in this print list we see new add value of list
print(saarc)
#here we use sort() method for showing list values chronologically
saarc.sort()
#now we see chronological values of list
print(saarc)
#here we use reverse() method for seeing values of list reversly
li=[1,2,3,4,5,6,7,8,9,10]
print(li)
li.reverse()
#this print line showa values of list reversly
print(li)
#this is another list for values
fruit=["jack-fruit","nuts","orange","apple","banana","mango"]
print(fruit)
#here we use insert() method for add new value in any where in list
fruit.insert(1,"papaw")
print(fruit)
#here we use now remove() method for delete list data
print(fruit)
#suppose now we want to delete nuts,then
fruit.remove("nuts")
print(fruit)
#now we use pop() method to return the last value of list and also remove from list
print(fruit)
fruit.pop()
print(fruit)
#here we use extend() method for connect tow list
li1=[1,2,3,4,5]
li2=[6,7,8,9,10]
li1.extend(li2)
#in this print line we see that li1 and li2 list is connected with each other
print(li)
#here we use count() method for find the value existing number in list
li=[1,2,3,4,4,4,5,6,5,7]
print(li)
#count() method
li.count(4)
#now we use del() method for delete data from list
print(li)
del(li[0])
print(li)
#here we use joint() method
#joint() method add the all strings
li=["a","b","c","d"]
print(li)
#str="".joint(li)
#str=",".joint(li)
#str="-".joint(li)
#here we do or more process by using list
li1=[1,2,3]
li2=[4,5,6]
#add process
li=li1+li2
print(li)
#minus process is not allowed
#li=l1-l2
#print(li)
#multiple process
li=li1+li2
print(li)
#divission process is not allowed
#li=l1/l2
#print(li)
#example of other data structure of python                        

# list = ["1","2","3","4","5"] --list is a mutable data structure

# tuple = (1,2,3,4,5,6) --tuple is non-mutable data structure

# set = {"pen","eraser","latop","mouse","keyboard"} -- its is set data structure of python

# Dictionary = [77,78,79,"Rajib","life",99,100] --its also data structure of python

#here we see dictionary data structure
Dictionary= {1:"rajib",2:78,4:99,3:100,5:"life"}
roll=input("please enter your roll number:")
roll=int(roll)
roll=str(roll)
print("this is for you:",Dictionary[int(roll)])

#here we see set data structure

items={"cellphone","laptop","pen"}
print(items)
#here we use type() method for see the data type of items
type(items)

#here we see tuple data structure

item=(1,2,3,4,5)
type(item)

#here we use split() method
#if we want to see the tottal string separately then use this split() method

str ="i am a programmer"
words= str.split()
print(words) 

