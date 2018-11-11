import math
num = int(input())
for i in range(num):
    a, b, c = map(int, input().split())
    if a+b > c and b+c > a and a+c > b:
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print('Area =', '%.3f' % area)
    else:
        print('Area of triangle is not possible! ')