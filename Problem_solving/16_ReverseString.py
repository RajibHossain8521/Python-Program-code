num = int(input())

for x in range(num):
    str = input()
    length = len(str)
    for i in range(length):
        if str[i] == "":
            result = str[::-1]
            result += str[i]
            print(result)

            # UNCOMPLETE
