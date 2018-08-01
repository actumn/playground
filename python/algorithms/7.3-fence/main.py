
def brute_force(h):
    ret = 0
    N = len(h)
    for left in range(N):
        minHeight = h[left]
        for right in range(left, N):
            minHeight = min(minHeight, h[right])
            ret = max(ret, minHeight * (right - left + 1))

    return ret


def solve(h, left, right):
    if left == right:
        return h[left]

    mid = int((left + right) / 2)

    ret = max(solve(h, left, mid), solve(h, mid+1, right))

    # 모두 걸치는 중간 것.
    lo, hi = mid, mid+1
    height = min(h[lo], h[hi])

    ret = max(ret, height * 2)

    while left < lo or hi < right:
        if hi < right and (lo == left or h[lo-1] < h[hi+1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1
            height = min(height, h[lo])

        ret = max(ret, height * (hi - lo + 1))

    return ret



C = int(input())
for _ in range(C):
    N = int(input())
    height_list = [int(elem) for elem in input().split()]
    print(solve(height_list, 0, N-1))
