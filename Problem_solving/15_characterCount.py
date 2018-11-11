# Character count of string in order form

num = int(input())

for i in range(num):
    char = input()
    length = len(char)
    for i in range(length):
        if char[i] >= 'a' and char[i] <= 'z':
           totalChar = char.count(char[i])
           print(char[i], '=', totalChar)

           # UNCOMPLETE