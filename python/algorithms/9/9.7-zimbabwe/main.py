# digits: e의 자릿수들을 정렬한 것.
e, digits = "", ""
n, m = 0, 0

def generate(price, taken):
    if len(price) == n:
        if price < e:
            print(price)

        return

    for i in range(n):
        if not taken[i] and (i == 0 or digits[i-1] != digits[i] or taken[i-1]):
           taken[i] = True
           generate(price + digits[i], taken)
           taken[i] = False


_mod = 10000000007
cache = {}

# 과거 가겨을 앞 자리 부터 채워나가고 있다.
# index: 이번에 채울 자리의 인덱스
# taken: 지금까지 사용한 자릿수들의 집합
# mode: 지금까지 만든 가격의 m에 대한 나머지
# less: 지금까지 만든 가격이 이미 e보다 작으면 1, 아니면 0
def price(index, taken, mod, less):
    if index ==n:
        return 1 if less and mod == 0 else 0

    if (taken, mod, less) in cache:
        return cache[(taken, mod, less)]

    ret = 0
    for next in range(n):
        if (taken & (1 << next)) == 0:
            # 과거 가격은 새 가격보다 항상 작아야 한다.
            if not less and e[index] < digits[next]:
                continue

            # 같은 숫자는 한 번만 선택한다.
            if next > 0 and digits[next-1] == digits[next] and (taken & (1 << next-1)) == 0:
                continue

            next_taken = taken | (1 << next)
            next_mod = (mod * 10 + int(digits[next])) % m
            next_less = less or e[index] > digits[next]
            ret += price(index + 1, next_taken, next_mod, next_less)
            ret %= _mod

    cache[(taken, mod, less)] = ret
    return ret


for _ in range(int(input())):
    e, m = map(str, input().split())
    m = int(m)
    n = len(e)
    digits = ''.join(sorted(e))

    # taken = [False for _ in range(15)]
    # generate('', taken)

    print(price(0, 0, m, False))
    cache = {}
