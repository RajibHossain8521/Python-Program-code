# For sequence the number Small to Large

num = int(input())

if num in range(0, 100):
    for i in range(num):
        n1, n2, n3 = map(int, input().split(' '))
        for j in range(num):
            j += 1
            if n1 < n2:
                temp = n1
            else:
                temp = n1
                n1 = n2
                n2 = temp
            if n1 < n3:
                temp = n1
            else:
                temp3 = n3
                n3 = n1
                n1 = temp3
            if n2 < n3:
                temp2 = n2
            else:
                temp3 = n3
                n3 = n2
                n2 = temp3
            print('Case', j, ':', n1, n2, n3, end=' ')
            print()
            break











