n = 0
board = [[0] * 100 for _ in range(100)]

# brute force
def jump(y, x):
    if y >= n or x >= n:
        return False

    if y == n-1 and x == n-1:
        return True

    jump_size = board[y][x]

    return jump(y + jump_size, x) or jump(y, x + jump_size)


# memoization
cache = {}
def jump2(y, x):
    if y >= n or x>= n:
        return 0

    if y == n-1 and x == n-1:
        return 1

    if (y, x) in cache:
        return cache[(y, x)]

    jump_size = board[y][x]
    ret = jump2(y + jump_size, x) + jump2(y, x + jump_size)
    cache[(y,x)] = ret

    return ret
