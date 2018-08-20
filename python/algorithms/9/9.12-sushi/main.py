n, m = 0, 0
price, pref = [], []

cache = {}
def sushi(budget):
    if budget in cache:
        return cache[budget]

    ret = 0
    for dish in range(n):
        if budget < price[dish]:
            continue

        ret = max(ret, sushi(budget - prcie[dish]) + pref[dish])

    return ret

c = [0]
def sushi2():
    ret = 0
    for budget in range(1, m+1):
        c[budget] = 0
        for dish in range(n):
            if budget >= price[dish]:
                c[budget] = max(c[budget], c[budget - price[dish]] + pref[dish])

        ret = max(ret, c[budget])

    return ret

c = [0 for _ in range(201)]
def sushi3():
    ret = 0
    c[0] = 0
    for budget in range(1, m+1):
        cand = 0
        for dish in range(n):
            if budget >= price[dish]:
                cand = max(cand, c[(budget - price[dish]) % 201] + pref[dish])

        c[budget % 201] = cand
        ret = max(ret, cand)

    return ret


for _ in range(int(input())):
    n, m = map(int, input().split())
    m = m / 100
    for _ in range(n):
        one_price, one_prefer = map(int, input().split())
        one_price = one_price / 100
        price.append(one_price)
        pref.append(one_prefer)

