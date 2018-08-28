import queue

def concat(lengths):
    pq = queue.PriorityQueue()
    for length in lengths:
        pq.put(length)

    ret = 0
    while pq.qsize() > 1:
        min1 = pq.get()
        min2 = pq.get()
        pq.put(min1 + min2)
        ret += min1 + min2

    return ret


for _ in range(int(input())):
    n = int(input())
    lengths = list(map(int, input().split()))
    print(concat(lengths))
