_mod = 1000000007
cache = {}

def tiling(width):
    if width == 0 or width == 1:
	    return 1

    if width in cache:
        return cache[width]

    ret = (tiling(width-2) + tiling(width-1)) % _mod
    cache[width] = ret
    return ret

C = int(input())
for _ in range(C):
    N = int(input())
    print(tiling(N))
    cache = {}
