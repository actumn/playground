import math

n = 0
m, q = map(int, input().split())
corpus = list(map(str, input().split()))
B = list(map(float, input().split()))
# 확률 로그를 저장해야함.
T, M = [], []

R = []
choice = [[0] * 502 for _ in range(102)]
cache = {}

def recognize(segment, previous_match):
    if segment == n:
        return 0

    if (segment, previous_match) in cache:
        return cache[(segment, previous_match)]

    ret = -1e200
    choose = choice[segment][previous_match]
    for this_match in range(m):
        cand = T[segment][this_match] + M[this_match][R[segment]] + recognize(segment+1, this_match)
        if ret < cand:
            ret = cand
            choose = this_match

    choice[segment][previous_match] = choose

    cache[(segment, previous_match)] = ret
    return ret



def reconstruct(segment, previous_match):
    choose = choice[segment][previous_match]
    ret = corpus[choose]
    if segment < n-1:
        ret = ret + " " + reconstruct(segment + 1, choose)

    return ret



for _ in range(m):
    T += [[math.log(float(elem)) if float(elem) > 0.0 else -1e200 for elem in input().split()]]

for _ in range(m):
    M += [[math.log(float(elem)) if float(elem) > 0.0 else -1e200 for elem in input().split()]]

for _ in range(q):
    _input = input().split()
    n = int(_input[0])
    r = _input[1:]
    for r_item in r:
        R.append(corpus.index(r_item));

    print(recognize(0, 0))
    print(reconstruct(0, 0))
    cache = {}
    choice = [[0] * 502 for _ in range(102)]


