def pick(n, picked, toPick):
    if toPick == 0:
        print(picked)
        return;

    smallest = picked[-1] + 1 if picked else 0

    for number in range (smallest, n):
        picked.append(number)
        pick(n, picked, toPick-1)
        picked.pop()

    return


pick(5, [], 3)
