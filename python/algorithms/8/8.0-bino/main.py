def bino(n, r):
    if r == 0 or n == r:
        return 1

    return bino(n-1, r-1) + bino(n-1, r)

cache = {}
def bino2(n, r):
    if r == 0 or n == r:
        return 1

    if (n, r) in cache:
        return cache[(n, r)]

    ret = bino2(n-1, r-1) + bino(n-1, r)
    cache[(n, r)] = ret
    return ret

print(bino(5,2))
print(bino2(5,2))
