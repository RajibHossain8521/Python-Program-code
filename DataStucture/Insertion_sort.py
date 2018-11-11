# Insertion sort

# for checking the function or program execute time and memory space

# from profilehooks import profile
# from memory_profiler import profile

# Function for insertion sort
# @profile


def insertion_sort(L):
    # this below statement find the length of list
    n = len(L)

    for i in range(1, n):
        # Assigning the L[i] value in Item Variable
        item = L[i]

        # now find the right place for item
        j = i - 1

        while j >= 0 and L[j] > item:
            # now keep the L[j] index value in (j+1) index
            L[j+1] = L[j]
            j = j-1
            # L[j+1] is the right place for item
            # and we are already empty this index
            L[j+1] = item


if __name__ == '__main__':
    L = [6, 1, 4, 9, 2]
    print('Before sort:', L)
    insertion_sort(L)
    print('After sort:', L)




