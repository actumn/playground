n = 0
dist = {}
cache = {}
INF = 1000000007

def shortest_path2(here, visited):
    # 모두 방문한 케이스
    if visited == (1 << n) - 1:
        return dist[here][0]

    if (here, visited) in cache:
        return cache[(here, vistied)]

    ret = INF
    for next in range(n):
        if visited & (1 << next):
            continue

        cand = dist[here][next] + shortest_path2(next, visited + (1 << next))
        ret = min(ret, cand)

    return ret
