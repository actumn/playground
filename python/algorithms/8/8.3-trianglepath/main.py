n = 5
triangle = [
    [1, 0, 0, 0, 0],
    [2, 4, 0, 0, 0],
    [8, 16, 8, 0, 0],
    [32, 64, 32, 64, 0],
    [128, 256, 128, 256, 128]
]
#[[0] * 100 for _ in range(100)]



cache = {}
def path1(y, x, sum):
    if y == n-1:
        return sum + triangle[y][x]

    if (y, x, sum) in cache:
        return cache[(y, x, sum)]

    sum += triangle[y][x]
    ret = max(path1(y+1, x+1, sum), path1(y+1, x, sum))
    cache[(y, x, sum)] = ret

    return ret


cache2 = {}
def path2(y, x):
    if y == n-1:
        return triangle[y][x]

    if (y, x) in cache2:
        return cache2[(y, x)]

    ret = max(path2(y+1, x), path2(y+1, x+1)) + triangle[y][x]
    cache2[(y,x)] = ret
    return ret


import time

start_time_path1 = time.time()
print(path1(0, 0, 0))
print(f"path1 running time: {time.time() - start_time_path1}")
start_time_path2 = time.time()
print(path2(0,0))
print(f"path2 running time: {time.time() - start_time_path2}")
