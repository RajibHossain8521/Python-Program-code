testCase = int(input())
for i in range(testCase):
    num = int(input())
    temp = num
    result = 0
    while temp != 0:
        rem = temp % 10
        result += rem*rem*rem
        temp //= 10
    if result == num:
        print(num, 'is an armstrong number!')
    else:
        print(num, 'is not armstrong number!')





