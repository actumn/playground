

def order(russian, korean):
    wins = 0

    russian.sort(reverse=True) # nlogn
    for cur_russian in russian:
        for cur_korean in korean:
            if cur_russian < cur_korean:
                wins += 1
                korean.remove(cur_korean)
                break

    return wins



russian = [3000, 2700, 2800, 2200, 2500, 1900]
korean = [2800, 2750, 2995, 1800, 2600, 2000]
print(order(russian, korean))
