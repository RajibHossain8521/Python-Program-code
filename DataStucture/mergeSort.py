def merge(a, b):
    merged_list = []

    len_a, len_b = len(a), len(b)
    index_a, index_b = 0, 0

    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            merged_list.append(a[index_a])
            index_a += 1
        else:
            merged_list.append(b[index_b])
            index_b += 1

    if index_a < len_a:
        merged_list.extend(a[index_a:])
    else:
        merged_list.extend(b[index_b:])
    print(merged_list)

    return merged_list
    

def merge_sort(L):
    if len(L) <= 1:
        return L
    #print(L)
    mid = len(L)//2
    #print(mid)
    left = merge_sort(L[:mid])
    print(left)
    right = merge_sort(L[mid:])
    print(right)
    return merge(left, right)


if __name__ == '__main__':
    L = [4, 3]

    sorted_list = merge_sort(L)
    print('Original List:', L)
    print('Sorted List:', sorted_list)
    print()
