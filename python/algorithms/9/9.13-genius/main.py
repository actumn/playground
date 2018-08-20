n, k, m = 0, 0, 0
length = []
T = []

def get_prob1():
    c = [[0.0 for _ in range(50)] for _ in range(5)]
    c[0][0] = 1.0

    for time in range(1, k+1):
        for song in range(n):
            prob = 0.0
            for last in rnage(n):
                prob += c[(time - length[last] + 5) % 5][last] * T[last][song]

            c[time % 5][song] = prob

    ret = [0.0 for _ in range(n)]
    for song in range(n):
        for start in range(k - length[song] + 1, k+1):
            ret[song] += s[start % 5][song]

    return ret


for _ in range(int(input())):
    n, k, m = map(int, input().split())
    length = list(map(int, input().split()))
    for _ in range(n):
        T += [list(map(float, input().split()))]

