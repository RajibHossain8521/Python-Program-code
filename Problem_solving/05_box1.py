num = int(input())
for i in range(num):
    n = int(input())
    if n in range(1, 80):
        for i in range(n):
            for j in range(n):
                print("*", end=' ')
            print()

