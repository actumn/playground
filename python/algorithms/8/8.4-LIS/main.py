
def lis(A):
    if not A:
        return 0

    ret = 0
    for index in range(len(A)):
        B = []
        for next_index in range(index + 1, len(A)):
            if A[index] < A[next_index]:
                B += [A[next_index]]

        ret = max(ret, 1 + lis(B))

    return ret



n = 0
cache = {}
S = []
def lis2(start):
    if start in cache:
        return cache[start]

    ret = 1
    for next in range(start+1, n):
        if S[start] < S[next]:
            ret = max(ret, lis2(next) + 1)

    return ret




n = 0
cache = {}
S = []
def lis3(start):
    if start+1 in cache:
        return cache[start+1]

    ret = 1
    for next in range(start+1, n):
        if start == -1 or S[start < S[next]:
            ret = max(ret, lis3(next) + 1)

    cache[start+1] = ret
    return ret
