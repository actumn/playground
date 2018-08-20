n, board = 0, []

cache = {}
def play(left, right):
    # 기저 사례
    if left > right:
        return 0

    if (left, right) in cache:
        return cache[(left, right)]

    # 수를 가져오는 경우
    ret = max(board[left] - play(left + 1, right), board[right] - play(left, right-1))
    # 수를 없애는 경우
    if (right - left + 1) >= 2:
        ret = max(ret, -play(left + 2, right))
        ret = max(ret, -play(left, right -2))

    cache[(left, right)] = ret
    return ret


for _ in range(int(input())):
    n = int(input())
    board = list(map(int, input().split()))
    print(play(0, n-1))
    cache = {}
