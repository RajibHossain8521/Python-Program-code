num = int(input())
for i in range(num):
     str = input()
     length = len(str)
     count = 0
     for x in range(length):
        if str[x] == 'a' or str[x] == 'e' or str[x] == 'i' or str[x] == 'o' or str[x] == 'u':
            print(str[x], end="")
     print('\n')

     for x in range(length):
        if str[x] != 'a' and str[x] != 'e' and str[x] != 'i' and str[x] != 'o' and str[x] != 'u':
            print(str[x], end="")
     print('\n')

