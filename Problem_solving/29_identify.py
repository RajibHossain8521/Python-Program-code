num = int(input())
for i in range(num):
    ch = input()
    if ch >= 'a' and ch <= 'z':      # When we compare something with something others
        print('Lowercase Character')  # then must be care about '=' operator

    elif ch >= 'A' and ch <= 'Z':
        print('Upercase Character')

    elif ch >= '0' and ch <= '9':
        print('Numerical Number')

    else:
        print('Special Character')
