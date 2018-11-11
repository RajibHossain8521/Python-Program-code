t = int(input())
for i in range(t):
    n = int(input())
    if n in range(1, 100000):
        for j in range(1, n+1):
            if n % j == 0:
                print(j, end=' ')
                # j += 1
        print()
