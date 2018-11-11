num = int(input())
for i in range(num):
    x = int(input())
    n = int(input())
    if x > n:
        print('Invalid!')
    for j in range(x, n+1):
        if j % x == 0:
            print(j)

