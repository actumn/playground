connected = []
deg = []
N, D, P = 0, 0, 0

cache = {}
def search2(here, days):
    if days == D:
        return 1.0 if here == P else 0.0

    if (here, days) in cache:
        return cache[(here, days)]

    ret = 0.0
    for there in range(N):
        if connected[here][there]:
            ret += search2(there, days+1) / deg[there]

    return ret

for _ in range(int(input())):
    N, D, P = map(int, input().split())
    for _ in range(N):
        con = [int(elem) for elem in input().split()]
        connected.append(con)
        deg.append(con.count(1))

    T = int(input())
    Q = [int(elem) for elem in input().split()]
    ret = []
    for q in Q:
        ret += [search2(q, 0)]

    print(ret)
    cache = {}



