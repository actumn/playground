skip = 10

def generate(n, m, s):
    if n == 0 and m == 0:
        print(s)
        return

    if n > 0:
        generate(n-1, m, s + "-")

    if m > 0:
        generate(n, m-1, s + "o")


def generate2(n, m, s):
    global skip
    if skip < 0:
        return

    if n == 0 and m == 0:
        if skip == 0:
            print(s)

        skip -= 1
        return


    if n > 0:
        generate2(n-1, m, s + "-")

    if m > 0:
        generate2(n, m-1, s + "o")


Max = 1000000000 + 100
bino = [[0] * 201 for _ in range(201)]
def calc_bino():
    for i in range(201):
        bino[i][0] = bino[i][i] = 1
        for j in range(1, i):
            bino[i][j] = min(Max, bino[i-1][j-1] + bino[i-1][j])

def generate3(n, m, s):
    global skip
    if skip < 0:
        return

    if n == 0 and m == 0:
       if skip == 0:
           print(s)

       skip -= 1
       return

    if bino[n+m][n] <= skip:
        skip -= bino[n+m][n]
        return

    if n > 0:
        generate3(n-1, m, s + "-")

    if m > 0:
        generate3(n, m-1, s + "o")



def kth(n, m, skip):
    if n == 0:
        return "o" * m

    if skip < bino[n+m-1][n-1]:
        return "-" + kth(n-1, m, skip)

    return "o" + kth(n, m-1, skip - bino[n+m-1][n-1])

calc_bino()
generate3(3, 3, '')
print(kth(3, 3, 10))
