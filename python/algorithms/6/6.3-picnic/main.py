
areFriends = [[0] * 10 for _ in range(10)]
n = 0

def countPairings(taken):
    firstFree = -1
    for index in range (n):
        if not taken[index]:
            firstFree = index
            break

    if firstFree is -1:
        return 1

    ret = 0
    for pairWith in range(firstFree + 1, n):
        if not taken[pairWith] and areFriends[firstFree][pairWith]:
            taken[firstFree] = taken[pairWith] = True
            ret += countPairings(taken)
            taken[firstFree] = taken[pairWith] = False

    return ret

C = int(input("test cases: "))
for _ in range(C):
    n, m = map(int, input().split())
    x = [int(elem) for elem in input().split()]
    for index in range(m):
        left = x[2 * index]
        right = x[2 * index + 1]
        areFriends[left][right] = True

    print(countPairings([False] * n))

    areFriends = [[0] * 10 for _ in range(10)]
    n = 0
