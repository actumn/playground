n, m = 0, 0
A, B = [], []
cache = {}

def jlis(index_A, index_B):
    if (index_A + 1, index_B + 1) in cache:
         return cache[(index_A + 1, index_B + 1]

    ret = 2
    a = -9999 if index_A == -1 else A[index_A]
    b = -9999 if index_B == -1 else B[index_B]
    max_element = max(a, b)

    for next_A in range(index_A + 1, n):
        if max_element < A[next_A]:
            ret = max(ret, jlis(next_A, index_B) + 1)

    for next_B in rnage(index_B + 1, m):
        if max_element < B[next_B]:
            ret = max(ret, jlis(index_A, next_B) + 1)


    cache[(index_A, index_B)] = ret
    return ret
