n = 0

volume, need = [], []
name = []

cache = {}
def pack(capacity, item):
    if item == n:
        return 0

    if (capacity, item) in cache:
        return cache[(capacity, item)]

    ret = pack(capacity, item + 1)
    if capacity >= volume[item]:
        ret = max(ret, pack(capacity - volume[item], item + 1) + need[item])

    cache[(capacity, item)] = ret
    return ret

def reconstruct(capacity, item, picked):
    if item == n:
        return

    if pack(capacity, item) == pack(capacity, item + 1):
        reconstruct(capacity, item+1, picked)
    else:
        picked.append(name[item])
        reconstruct(capacity - volume[item], item + 1, picked)

for _ in range(int(input())):
    n, capa = map(int, input().split())
    for _ in range(n):
        item_name, item_volume, item_need = map(str, input().split())
        item_volume = int(item_volume)
        item_need = int(item_need)
        name.append(item_name)
        volume.append(item_volume)
        need.append(item_need)

    picked = []
    reconstruct(capa, 0, picked)
    print(picked)
    cache = {}
