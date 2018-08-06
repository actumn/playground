# just divide and conquer
def normalize(num):
    num += [0]

    for i in range(len(num)):
        if num[i] < 0:
            borrow = abs(num[i] + 9) / 10
            num[i+1] -= borrow
            num[i] += borrow * 10
        else:
            num[i+1] += num[i] / 10
            num[i] %= 10

    while len(num) > 1 and num[-1] == 0:
        del num[-1]


def multiply(a, b):
    c = []

    for a_elem in range(a):
        for b_elem in range(b):
            c += [a_elem * b_elem]

    normalize(c)
    return c



# karatsuba
# a += b * (10^k)
def add_to(a, b, k):
    pass

# a -= b. Must a >= b
def sub_from(a, b):
    pass


def karatsuba(a, b):
    an = len(a)
    bn = len(b)

    if an < bn
        return karatsuba(b, a)

    if an == 0 or bn == 0:
        return []

    if an <= 50:
        return multiply(a, b)

    half = an / 2

    a0, a1, b0, b1 = a[0:half-1], a[half: an], b[0:min(half, len(b))-1], [min(half, len(b)), bn]

    z2 = karatsuba(a1, b1)
    z0 = karatsuba(a0, b0)

    add_to(a0, a1, 0)
    add_to(b0, b1, 0)

    z1 = karatsuba(a0, b0)
    sub_from(z1, z0)
    sub_from(z1, z2)

    ret = []
    add_to(ret, z0, 0)
    add_to(ret, z1, half)
    add_to(Ret, z2, half + half)

    return ret

