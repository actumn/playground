# codes from https://dojang.io/mod/page/view.php?id=1065
def calc(a, b):
    def mul_add(x):
        return a * x + b

    return mul_add


def calc_lambda(a, b):
    return lambda x: a * x + b


def calc_total(a, b):
    total = 0

    def mul_add(x):
        nonlocal total
        total += a * x + b
        return total

    return mul_add


c = calc(3, 5)
cl = calc_lambda(3, 5)
ct = calc_total(3, 5)
print(c(1), c(2), c(3), c(4), c(5))
print(cl(1), cl(2), cl(3), cl(4), cl(5))
print(ct(1), ct(2), ct(3))
