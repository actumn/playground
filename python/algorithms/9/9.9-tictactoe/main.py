
def is_finished(board, turn):
    pass

# board가 주어졌을때 board를 int로 표현. 메모이제이션을 위해
def bijection(board):
    ret = 0
    for y in range(3):
        for x in range(3):
            ret = ret * 3
            if board[y][x] == 'o':
                ret += 1
            elif board[y][x] == 'x':
                ret += 2

    return ret


cache = {}
def can_win(board, turn):
    # 기저 사례: 마지막에 상대가 둬서 한 줄이 만들어진 경우
    if is_finished(board, turn):
        return -1

    board_status = bijection(board)
    if board_status in cache:
        return cache[board_status]

    min_value = 2
    for y in range(3):
        for x in range(3):
            if board[y][x] == '.':
                board[y][x] = turn
                min_value = min(min_value, can_win(board, 'o'+'x'-turn))
                board[y][x] = '.'

    # 비기는 것이 최선
    if min_value == 2 or min_value == 0:
        ret = 0
        cache[board_status] = ret
        return ret

    # 상대가 이기면 난 지고, 상대가 진다면 난 이긴다.
    ret = -min_value
    cache[board_status] = ret
    return ret
