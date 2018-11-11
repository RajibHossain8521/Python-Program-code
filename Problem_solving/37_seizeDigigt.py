"""
num = int(input())
for i in range(num):
    n = int(input())
    rev = 0
    for i in range(n):
        rev = rev * 10
        rev = rev + n % 10
        n = n / 10
    print(rev)
"""

""" In this Program my output print 'inf' instead of number """

# Other Technique to change int into string and reverse
"""
num = int(input())
for i in range(num):
    n = input()
    result = n[::-1]
    print(result)
"""
# now using loop

num = int(input())
for i in range(num):
    text = input()  # we also input 'int' number and cast it into 'str'
    length = len(text)
    text_rev = ""
    while length > 0:
        text_rev = text_rev + text[length - 1]
        length = length - 1
    print(text_rev)

