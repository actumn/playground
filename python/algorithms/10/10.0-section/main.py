n = 0
begin, end = [], []

def schedule():
    order = []
    for index in n:
        order.append((begin[index], end[index]))

    order.sort()

    earliest, selected = 0, 0
    for section in order:
        meeting_begin, meeting_end = section[1], section[0]
        if earliest <= meeting_begin:
            earliest = meeting_end
            selected += 1

    return selected
