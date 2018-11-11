num = int(input())
for i in range(num):
    a = int(input())
    b = int(input())
    c = int(input())
    for j in range(1, c+1):
        if j % a == 0 and j % b == 0:
            print(j)


