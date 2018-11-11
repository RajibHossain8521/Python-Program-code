# for Selection sort


def selecttion_sort(L):
    n = len(L) # Here i find the List length and assign in n variable

    for i in range(0, n-1):
        index_min = i

        for j in range(i+1, n):
            if L[j] < L[index_min]:
                index_min = j

        if L[index_min] != i:
            L[i], L[index_min] = L[index_min], L[i]


if __name__ == '__main__':
    L = [6, 1, 4, 9, 2]
    print('Before sort:', L)
    selecttion_sort(L)
    print('After sort:', L)

