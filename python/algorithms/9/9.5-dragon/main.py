_max = 1000000000 + 1
length = []

def precalc():
    global length
    length += [1]
    for i in range(1, 50):
        length += [min(_max, length[i-1] * 2 + 2)]


expand_x = "X+YF"
expand_y = "FX-Y"

def expand(dragon_curve, generations, skip):
    if generations == 0:
        assert(skip < len(dragon_curve))
        return dragon_curve[skip]

    for s in dragon_curve:
        if s == 'X' or s == 'Y':
            if skip >= length[generations]:
                skip -= length[generations]
            elif s == 'X':
                return expand(expand_x, generations-1, skip)
            else:
                return expand(expand_y, generations-1, skip)
        elif skip > 0:
            skip -= 1
        else:
            return s

    return "not reached"


precalc()
for _ in range(int(input())):
    n, p, l = map(int, input().split())
    for index in range(l):
        print(expand("FX", n, p + index - 1), end='')

    print()
