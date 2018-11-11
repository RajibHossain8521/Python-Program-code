num = int(input())
for i in range(num):
    n = int(input())
    if n > 1:
        for j in range(2, n):
            print(j)
            if n % j == 0:
                print(n, 'is not a prime')
                break
        else:
            print(n, 'is a prime')
    else:
        print(n, 'is not a prime')

# time complexity of this program  O(n)

