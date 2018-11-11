# Function for Linear_search


def linear_search(L, x):
    n = len(L)
    i = 0

    while i < n:
        if L[i] == x:
            return i
        i += 1

    i = -1
    return i


if __name__ == "__main__":
    L = [1, 2, 5, 765, 4, 6, 0, 9, 34]
    result = linear_search(L, 9)
    print(result)


