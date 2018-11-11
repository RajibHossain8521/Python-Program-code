"""
num = int(input())
for i in range(num):
    n = input()
    length = len(n)
    palindrome = ""
    while length > 0:
        palindrome = palindrome + n[length-1]
        print(palindrome)
        length = length - 1
    if palindrome == n:
        print('YES, it is palindrome!')
    else:
        print('SORRY, it is not palindrome!')

"""

# Without Using Loop

testCase = int(input())
for i in range(testCase):
    string = input()
    palindrome = string[::-1]
    if palindrome == string:
        print('YES, it is Palindrome')
    else:
        print('N0, it is not Palindrome')