cache = {}
W, S = "", ""

def match_memoized(w, s):
    if (w, s) in cache:
        return cache[(w, s)]

    while s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
        w += 1
        s += 1

    if w == len(W):
        ret = 1 if s == len(S) else 0
        cache[(w, s)] = ret
        return ret

    if W[w] == '*':
        for skip in range(s, len(S)):
            if match_memoized(w+1, skip):
                ret = 1
                cache[(w, s)] = ret
                return ret

    return 0


C = int(input())
for _ in range(C):
    W = input()
    N = int(input())
    for _ in range(N):
        S = input()
        if match_memoized(0, 0):
            print(S)


