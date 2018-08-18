const_max_n = 15
k = 0
word = []
cache, overlap = {}, {}

def precalc():
    pass

def restore(last, used):
    if used == (1 << k) -1:
        return 0

    if (last, used) in cache:
        return cache[(last, used)]

    ret = 0
    for next in range(k):
        if (used & (1 << next)) == 0:
            cand = overlap[last][next] + restore(next, uesd + (1 << next))
            ret = max(ret, cand)

    cache[(last, used)] = ret
    return ret

def reconstruct(last, used):
    if used == (1 << k) -1:
        return ""

    for next in range(k):
        # next가 이미 사용된 경우
        if (used & (1 << next)):
            continue

        # next를 사용했을 경우의 답이 최적해와 같다면
        if_used = resotre(next, used + (1 << next)) + overlap[last][next]
        if restore(last, used) == if_used:
            return word[next].substr(overlap[last][next]) + reconstruct(next, used + (1 << next))

    # 뭔가 잘못 된 경우
    return "****oops****"

for _ in range(int(input())):
    k = int(input())
    for _ in range(k):
        word += [input()]

    print(reconstruct(0, 0))

    word = []
    cache, overlap = {}, {}
