n = 0
e, m = [], []

def solve():
    order = []
    for index in range(n):
        order.append((m[index], e[index]))

    order.sort(reverse=True)

    ret, total_heat = 0, 0
    for item in order:
        total_heat += item[1]
        ret = max(ret, total_heat + item[0])

    return ret

for _ in range(int(input())):
    n = int(input())
    e = list(map(int, input().split()))
    m = list(map(int, input().split()))

    print(solve())
