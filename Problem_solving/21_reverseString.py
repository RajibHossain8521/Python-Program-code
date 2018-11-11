num = int(input())
for i in range(num):
    if i in range(0, 100):
        str = input()
        length = len(str)
        if length in range(0, 1000):

            result = str[::-1]
            print(result)

            # COMPLETE