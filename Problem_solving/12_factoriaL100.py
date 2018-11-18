def rec_factorial(n):
    if n == 1:
        return n
    else:
        return n*rec_factorial(n-1)


testCase = int(input())
for i in range(testCase):
    num = int(input())
    result = rec_factorial(num)
    count = 0
    while result > 0:
        zero = result % 10
        if zero == 0:
            count += 1
        result = result // 10

    print(count)


