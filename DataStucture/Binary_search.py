# For Binary search


def binary_search(L, x):
    left, right = 0, len(L)-1

    while left <= right:
        mid = (left + right)//2  # integer division

        if L[mid] == x:
            return mid

        if L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

"""
if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = binary_search(L, 9)
    print(result)
"""

if __name__ == '__main__':
    testCase = int(input())
    for i in range(testCase):
        lst = map(int, input().split())
        lsts = list(lst)
        find = int(input())

        position = binary_search(lsts, find)

        if position == -1:
            if find in lsts:
                print(find, 'is in L, but function returned -1')
            else:
                print(find, 'not in list')
        else:
            if position in lsts:
                print(find, 'found in list!.')

    print('program terminated')

'''if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for x in range(1, 11):
        position = binary_search(L, x)

        if position == -1:
            if x in L:
                print(x, 'is in L, but function returned -1')
            else:
                print(x, 'not in list')
        else:
            if L[position] == x:
                print(x, 'found in correct position.')
            else:
                print('binary search returned', position, 'for', x, 'which is incorrect')

    print('program terminated')
'''

# Binary Search using Recursive Function

'''
def binary_search_recursive(L, left, right, x):
    if left > right:
        return -1

    mid = (left + right) // 2

    if L[mid] == x:
        return mid
    if L[mid] < x:
        return binary_search_recursive(L, mid+1, right, x)
    else:
        return binary_search_recursive(L, left, mid-1, x)


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6, 7, 8]
    left = 0
    right = len(L) - 1

    for x in range(1, 11):
        position = binary_search_recursive(L, left, right, x)

        if position == -1:
            if x in L:
                print(x, 'is in L  but function returned -1')
            else:
                print(x, 'not in list')

        else:
            if L[position] == x:
                print(x, 'found correct position')
            else:
                print('binary search returned', position, 'for', x, 'which is not correct')

    print('Program Terminated!')
'''





















