# For find the sum of series number

# Without Loop
'''
num = int(input())

for i in range(num):
    n = int(input())
    if n in range(0, 65535):
        lsd = n % 10  # lsd = least significant digit
        #  print(lsd)
        fast = int(str(n)[0])
        result = fast + lsd
        print('sum = ', result)
'''


# Using Loop


num = int(input())

for i in range(num):
    n = int(input())
    if n in range(0, 65535):
        lsd = n % 10  # lsd = least significant digit
        #  print(lsd)
        while True:
            if n // 10 == 0:
                 break
            else:
                y = n // 10
                n = y
                msd = n % 10  # msd = most significant digit
        result = msd + lsd
        print('sum =', result)

