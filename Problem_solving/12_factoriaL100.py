# def rec_factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*rec_factorial(n-1)
#
#
# testCase = int(input())
# for i in range(testCase):
#     num = int(input())
#     result = rec_factorial(num)
#     count = 0
#     while result > 0:
#         zero = result % 10
#         if zero == 0:
#             count += 1
#         result = result // 10
#
#     print(count)


def rec_factorial(n):
     if n == 1:
         return n
     else:
         return n*rec_factorial(n-1)


def counts(r):
    count = 0
    while r > 0:
        zero = r % 10
        if zero == 0:
            count += 1
        r = r // 10

    print(count)


if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        num = int(input())
        res = rec_factorial(num)
        print(res)
        counts(res)
