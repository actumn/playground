N = ""
cache = {}

def memorize(begin):
    if begin == len(N):
        return 0

    if begin in cache:
        return cache[begin]

    ret = 99999999
    for L in range(3, 6):
        if begin + L <= len(N):
            ret = min(ret, memorize(begin + L) + classify(begin, begin + L -1))

    cache[begin] = ret
    return ret


def classify(a, b):
    M = N[a:b+1]

    if M == M[0] * len(M):
        return 1

    progressive = True
    for index in range(len(M)-1):
        if int(M[index+1]) - int(M[index]) != int(M[1]) - int(M[0]):
            progressive = False

    if progressive and abs(int(M[1]) - int(M[0])):
        return 2


    alternating = True
    for index in range(len(M)):
        if M[index] != M[index%2]:
            alternating = False

    if alternating:
        return 4

    if progressive:
        return 5

    return 10


C = int(input())
for _ in range(C):
    N = input()
    print(memorize(0))
    cache = {}
