n = 0
cache = {}
S = []
choices = [-1 for _ in range(101)]

def lis4(start):
    if start in cache:
        return cache[start]

    ret = 1
    best_next = -1
    for next in range(start+1, n):
        if start == -1 or S[start] < S[next]:
            cand = lis4(next) + 1
            if cand > ret:
                ret = cand
                best_next = next

    choices[start+1] = best_next

    cache[start] = ret
    return ret


def reconstruct(start, seq):
    if start != -1:
        seq.append(S[start])

    next = choices[start+1]
    if next != -1:
        reconstruct(next, seq)


