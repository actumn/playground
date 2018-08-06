board = [
    [9, 0, 0, 0],
    [5, 7, 0, 0],
    [1, 3, 2, 0],
    [3, 5, 5, 6]
]
n = 4
cache = {}
def pathcount(y, x):
    if y == n-1: 
        return 1
    
    if (y, x) in board:
        return board[(y, x)]
    
    ret = 0    
    if path2(y+1, x+1) >= path2(y+1, x):
        ret += pathcount(y+1, x+1)
    
    if path2(y+1, x+1) <= path2(y+1, x):
        ret += pathcount(y+1, x)
    
    cache[(y, x)] = ret
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
    
    