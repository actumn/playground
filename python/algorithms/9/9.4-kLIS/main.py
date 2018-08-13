_max = 2000000000 + 1
n = 0
S = []
cache_len, cache_count = {}, {}

# start에서 시작하는 lis 최대 길이
def lis(start):
    if start + 1 in cache_len:
        return cache_len[start+1]

    ret = 1
    for next in range(start+1, n):
        if start == -1 or S[start] < S[next]:
            ret = max(ret, lis(next) + 1)

    cache_len[start+1] = ret
    return ret

# start에서 시작하는 lis 개수
def count(start):
    if lis(start) == 1:
        return 1

    if start+1 in cache_count:
        return cache_count[start+1]

    ret = 0
    for next in range(start+1, n):
        if (start == -1 or S[start] < S[next]) and (lis(start) == lis(next) + 1):
            ret = min(_max, ret + count(next))

    cache_count[start+1] = ret
    return ret

def reconstruct(start, skip, ret):
    if start != -1:
        ret.append(S[start])

    followers = []
    for next in range(start+1, n):
        if (start == -1 or S[start] < S[next]) and (lis(start) == lis(next) + 1):
            followers.append((S[next], next))

    followers.sort()

    for i in range(len(followers)):
        idx = followers[i][1]
        cnt = count(idx)
        if cnt <= skip:
            skip -= cnt
        else:
            reconstruct(idx, skip, ret)
            break


for _ in range(int(input())):
    n, k = map(int, input().split())
    S = list(map(int, input().split()))

    ret = []
    reconstruct(-1, k, ret)
    print(len(ret))
    print(ret)
    cache_len = {}
    cache_count = {}
