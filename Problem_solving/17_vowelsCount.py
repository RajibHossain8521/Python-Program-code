num = int(input())
for i in range(num):
     str = input()
     length = len(str)
     count = 0
     for x in range(length):
        if str[x] == 'a' or str[x] == 'e' or str[x] == 'i' or str[x] == 'o' or str[x] == 'u':
            count = count + 1
     print('Numbers of vowels =', count)


                            # COMPLETE
