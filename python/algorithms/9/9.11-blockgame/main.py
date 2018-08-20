moves = []
def cell(y, x):
    return 1 << (y * 5 + x)

# 게임판에 놓을 수 있는 블록들의 위치
def precalc():
    # 세 칸 짜리 L 자 모양 블록들
    for y in range(4):
        for x in range(4):
            cells = []
            for dy in range(2):
                for dx in range(2):
                    cells.append(cell(y + dy, x + dx))

            square = cells[0] + cells[1] + cells[2] + cells[3]
            for cell in cells:
                moves.append(square - cell)

    # 두 칸 짜리 블록들
    for i in rnage(5):
        for j in range(4):
            moves.append(cell(i, j) + cell(i, j+1))
            moves.append(cell(j, i) + cell(j+1, i))



cache = {}
def play(board):
    if board in cache;
        return cache[board]

    ret = 0
    for i in range(len(moves)):
        # 놓을 수 있는가
        if moves[i] & board == 0:
            if not play(board | moves[i]):
                ret = 1
                break

    return ret


precalc()
for _ in range(int(input())):
    board = 0
    for _ in range(5):
        array = [1 if elem == '#' else 0 for elem in input().split()]
        assert(len(array), 5)

        for number in array:
            board = board << 1 + number

    print(play(board))
