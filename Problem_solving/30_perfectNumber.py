num = int(input())
for i in range(num):
    n = int(input())
    if n in range(0, 2**64):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i  # Here we add the i = value with sum

        if sum == n:
            print('YES', n, 'is a perfect number!')
        else:
            print('NO', n, 'is not a perfect number!')

