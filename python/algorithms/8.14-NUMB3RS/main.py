N, D, P = 0, 0, 0
q = 0

connected = []
deg = [0 for _ in range(51)]

def search(path):
    if len(path) == D:
        if path[-1] != q:
            return 0.0

        ret = 1.0
        for index in range(len(path)):
            ret /= deg[index]

        return ret

     ret = 0
     for there in range(N):
         if connected[path[-1]][there]:
             path.append(there)
             ret += search(path)
             del path[-1]

      return ret

for _ in range(int(input())):
    N, D, P = map(int, input().split())
    for _ in range(N):
        con = [int(elem) for elem in input().split()]
        connected.append(con)
        deg.append(con.count(1))

    T = int(input())
    Q = [int(elem) for elem in input().split()]
    ret = []
    for q in Q;
        ret += [search([])]

    print(ret)
