import math

num = int(input())
for i in range(num):
    x1, y1 = map(int, input().split())
    radius = int(input())
    x2, y2 = map(int, input().split())
    sqr1 = math.sqrt(x2-x1)
    sqr2 = math.sqrt(y2-y1)  # Here raise, ValueError:math domain error
    result = sqr1+sqr2
    distance = math.sqrt(result)
    if distance <= radius:
        print('The point is inside the circle')
    else:
        print('The point is not inside the circle')
