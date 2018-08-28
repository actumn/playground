import math

const_inf = 987654321

pi = 2 * math.acos(0)
n = 0
y, x, r = [], [], []
ranges = []

def convert_to_ranges():
    global ranges
    ranges = []

    for i in range(n):
        loc = math.fmod(2 * pi + math.atan2(y[i], x[i]), 2 * pi)
        range_i = 2 * math.asin(r[i] / 16)
        ranges.append((loc - range_i, loc + range_i))

    ranges.sort()


def solve_circular():
    ret = const_inf

    for range_i in ranges:
        if range_i[0] <= 0 or range_i[1] >= 2 * pi:
            begin = math.fmod(range_i[1], 2 * pi)
            end = math.fmod(range_i[0] + 2 * pi, 2 * pi)
            ret = min(ret, 1 + solve_linear(begin, end))

    return ret

def solve_linear(begin, end):
    used, idx = 0, 0

    while begin < end:
        max_cover = -1
        while idx < n and ranges[idx][0] <= begin:
            max_cover = max(max_cover, ranges[idx][1])
            idx += 1

        if max_cover <= begin:
            return const_inf

        begin = max_cover
        used += 1

    return used


for _ in range(int(input())):
    n = int(input())
    for _ in range(n):
        y_i, x_i, r_i = map(float, input().split())
        y += [y_i]
        x += [x_i]
        r += [r_i]

    convert_to_ranges()
    print(solve_circular())
