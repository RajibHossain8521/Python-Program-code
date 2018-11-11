# Max Heap Tree


def left(i):
    return 2*i


def right(i):
    return 2*i+1


def parent(i):
    return i // 2

'''
def is_max_heap(H):
    n = len(H) - 1

    for i in range(n, 1, -1):
        p = parent(i)

        if H[p] < H[i]: # H[p] is parent node and H[i] is child node
            return False # H[p],parent node less than it's child node H[i] ,than return False

    return True # else return True


if __name__ == '__main__':
    H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
    print(H, is_max_heap(H))
    H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 4]
    print(H, is_max_heap(H))
    H = [None, 1, 2, 3]
    print(H, is_max_heap(H))
    H = [None, 2, 3, 1]
    print(H, is_max_heap(H))
    H = [None, 3, 1, 2]
    print(H, is_max_heap(H))
'''

# We use three parameter in this function
    # 1st parameter(heap) for keeping the list
    # 2nd parameter(heap_size) for taking total element of list
    # 3rd parameter(i) is the index of node, from where function start his work
# function return nothing

#from binarytree import convert, pprint


def max_heapify(heap, heap_size, i):
    l = left(i)  # return 2*i
    r = right(i)  # return 2*i+1

    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i

    if r <= heap_size and heap[r] > heap[largest]:
        largest = r

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)


"""
# for max_heapify function
if __name__ == '__main__':
    h = [None, 19, 7, 12, 3, 5, 17, 10, 1, 2]
    print(h)
    max_heapify(h, 9, 3)
    print(h)
    print()
    h = [None, 1, 2, 3]
    print(h)
    max_heapify(h, 3, 1)
    print(h)
"""


def build_max_heap(heap):
    heap_size = len(heap) - 1

    for i in range(heap_size//2, 0, -1):
        max_heapify(heap, heap_size, i)



'''
def test_heap():
    heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    assert build_max_heap(heap) == [19, 10, 17, 5, 7, 12, 1, 2, 3]
'''


"""
# for build_max_heap function
if __name__ == '__main__':
    heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    print('Before building heap', heap)
    #pprint(convert(heap[1:]))
    build_max_heap(heap)
    print('After building heap', heap)
    #pprint(convert(heap[1:]))
"""


def heap_sort(heap):
    build_max_heap(heap)
    heap_size = len(heap) - 1

    for i in range(heap_size, 1 -1):
        heap[1], heap[i] = heap[i], heap[1]
        heap_size -= 1
        max_heapify(heap, heap_size, 1)


if __name__ == '__main__':
    heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    print('Before sorting', heap)
    heap_sort(heap)
    print('After sorting', heap)


















