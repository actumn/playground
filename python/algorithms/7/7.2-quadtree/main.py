def reverse(it):
    head = next(it)

    if head is 'b' or head is 'w':
        return head

    upperLeft = reverse(it)
    upperRight = reverse(it)
    lowerLeft = reverse(it)
    lowerRight = reverse(it)

    return "x" + lowerLeft + lowerRight + upperLeft + upperRight


C = int(input())
for _ in range(C):
    word = input()
    print(reverse(iter(word)))
