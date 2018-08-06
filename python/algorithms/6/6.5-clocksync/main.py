linked = [
    "xxx.............",
    "...x...x.x.x....",
    "....x.....x...xx",
    "x...xxxx........",
    "......xxx.x.x...",
    "x.x...........xx",
    "...x..........xx",
    "....xx.x......xx",
    ".xxxxx..........",
    "...xxx...x...x.."
]

def areAligned(clocks):
    for clock in clocks:
        if clock is not 12:
            return False

    return True


def push(clocks, switch):
    for clock in range(16):
        if linked[switch][clock] is 'x':
            clocks[clock] += 3
            if clocks[clock] is 15:
                clocks[clock] = 3

def solve(clocks, switch):
    if switch is 10:
        return 0 if areAligned(clocks) else 9999

    ret = 9999
    for cnt in range(4):
        ret = min(ret, cnt + solve(clocks, switch+1))
        push(clocks, switch)

    return ret


clocks = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
print(solve(clocks, 0))
