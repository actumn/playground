n = 0
A, p_sum, p_sq_sum = [], [], []

def precalc():
    A.sort()
    p_sum[0] = A[0]
    p_sq_sum[0] = A[0] * A[0]

    for index in range(1, n):
        p_sum[index] = p_sum[index-1] + A[i]
        p_sq_sum[i] = p_sq_sum[i-1] + A[i] * A[i]



def min_error(lo, hi):
    sum = p_sum[hi] - (0 if lo == 0 else p_sum[lo-1])
    sq_sum = p_sq_sum[hi] - (0 if lo == 0 else p_sq_sum[lo-1])

    m = int(0.5 + double(sum) / (hi - lo + 1))

    ret = sq_sum - 2 * m * sum + m * m * (hi - lo + 1)

    return ret


cache = {}
def quantize(begin, parts):
    if begin == n:
        return 0

    if parts == 0:
        return 99999999

    if (begin, parts) in cache:
        return cache[(begin, parts)]

    ret = 99999999
    for part_size in range(1, n+1):
        ret = min(ret, min_error(begin, begin + part_size - 1) + quantize(begin + part_size, parts - 1)

    cache[(begin, parts)] = ret
    return ret

