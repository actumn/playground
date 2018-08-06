Board = [
    ['U', 'R', 'L', 'P', 'M'],
    ['X', 'P', 'R', 'E', 'T'],
    ['G', 'I', 'A', 'E', 'T'],
    ['X', 'T', 'N', 'Z', 'Y'],
    ['X', 'O', 'Q', 'R', 'S']
]
dy = [-1, -1, -1, 1, 1, 1, 0, 0]
dx = [-1, 0, 1, -1, 0, 1, -1, 1]


def inRange(y, x):
    if x < 0 or x >= 8:
        return False

    if y < 0 or y >= 8:
        return False

    return True


def hasWord(y, x, word):
    if not inRange(y,x):
        return False

    if Board[y][x] is not word[0]:
        return False

    if len(word) is 1:
        return True

    for direction in range(0, 8):
        nextY = y + dy[direction]
        nextX = x + dx[direction]
        if hasWord(nextY, nextX, word[1:]):
            return True

    return False


print(hasWord(0, 0, "UPA"))
