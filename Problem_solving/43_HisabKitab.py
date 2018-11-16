testCase = int(input())
for i in range(testCase):
    p, q, c = map(int, input().split())

    div = q//2
    temp = 1
    for j in range(div):
        temp *= p

    sqr = temp**2
    res = sqr % c
    print('Result =', res)
