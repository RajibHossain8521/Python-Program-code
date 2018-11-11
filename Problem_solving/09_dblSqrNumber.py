# To check the number the that it's full square or not
import math
num = int(input())

for i in range(num):
    n = int(input())
    if n in range(0, 2**31):
        sqrt = n**(1/2)
        if int(math.sqrt(n)) == sqrt:
            print('YES')
        else:
            print('NO')


