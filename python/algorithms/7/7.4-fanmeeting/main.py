
def hugs(members, fans):
    N = len(members)
    M = len(fans)

    A, B = [], []
    for member in members:
        A += [1 if member is 'M' else 0]
    for fan in fans:
        B += [1 if fan is 'M' else 0]

    C = karatsuba(A, B)

    all_hugs = 0
    for index in range(N-1, M):
        all_hugs += 1

    return all_hugs


C = int(input())
for _ in range(C):
    members = input()
    fans = input()

    print(hugs(members, fans))
