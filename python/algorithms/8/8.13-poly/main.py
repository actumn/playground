MOD = 10 * 1000 * 1000
cache = {}

def poly(n, first):
    if n == first:
        return 1

    if (n, first) in cache:
        return cache[(n, first)]

    ret = 0
    for second in range(1, n - first + 1):
        add = int(second + first - 1)
        add *= int(poly(n-first, second))
        add %= MOD
        ret += add
        ret %= MOD

    cache[(n, first)] = ret
    return ret

C = int(input())
for _ in range(C):
    N = int(input())
    result = 0
    for first in range(N):
        result += poly(N, first + 1)

    result %= MOD
    print(result)
    cache = {}
