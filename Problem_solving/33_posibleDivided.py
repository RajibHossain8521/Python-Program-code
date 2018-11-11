num = int(input())
for i in range(num):
    a = int(input())
    b = int(input())
    c = int(input())
    for j in range(a, b+1):
        if j % c == 0:
            print(j)
