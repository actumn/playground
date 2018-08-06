_cover_type = [
    [ (0,0), (1,0), (0,1) ],
    [ (0,0), (0,1), (1,1) ],
    [ (0,0), (1,0), (1,1) ],
    [ (0,0), (1,0), (1,-1)]
]



# delta = 1 or -1
def set(board, y, x, type, delta):
    ok = True
    for index in range(3):
        CONST_ny = y + _cover_type[type][index][0]
        CONST_nx = x + _cover_type[type][index][1]
        if CONST_ny < 0 or CONST_ny >= len(board) or CONST_nx < 0 or CONST_ny >= len(board):
            ok = False
        else:
            board[CONST_ny][CONST_nx] = board[CONST_ny][CONST_nx] + delta
            if board[CONST_ny][CONST_nx] > 1:
                ok = False

    return ok


def cover(board):
    y = -1
    x = -1

    for rowIndex in range(len(board)):
        for colIndex in range(len(board[rowIndex])):
            if board[rowIndex][colIndex] is 0:
                y = rowIndex
                x = colIndex
                break

        if y is not -1:
            break

    print(f"y: {y}, x: {x}")

    if y is -1:
        return 1


    ret = 0
    for type in range(4):
        if set(board, y, x, type, 1):
            ret += cover(board)

        set(board, y, x, type, -1)

    return ret




_board = [
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1]
]


print(cover(_board))
