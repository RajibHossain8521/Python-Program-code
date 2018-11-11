num = int(input())

for i in range(num):
    n = int(input())
    if n in range(1, 15):
        fact = 1
        for x in range(1, n+1):
            fact = fact * n
            n -= 1
        print(fact)
