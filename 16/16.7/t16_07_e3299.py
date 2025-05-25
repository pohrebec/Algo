import sys
import threading

def main():
    sys.setrecursionlimit(1 << 25)
    n, m = map(int, sys.stdin.readline().split())
    parent_list = list(map(int, sys.stdin.readline().split()))
    a1, a2 = map(int, sys.stdin.readline().split())
    x, y, z = map(int, sys.stdin.readline().split())
    LOG = 17
    tree = [[] for _ in range(n)]

    for i in range(1, n):
        p = parent_list[i - 1]
        tree[p].append(i)

    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n

    def dfs(v, p):
        up[v][0] = p
        for i in range(1, LOG):
            if up[v][i - 1] != -1:
                up[v][i] = up[up[v][i - 1]][i - 1]
        for to in tree[v]:
            depth[to] = depth[v] + 1
            dfs(to, v)
    dfs(0, -1)

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for i in reversed(range(LOG)):
            if depth[u] - (1 << i) >= depth[v]:
                u = up[u][i]
        if u == v:
            return u
        for i in reversed(range(LOG)):
            if up[u][i] != -1 and up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]

    a = [0] * (2 * m + 1)
    a[1] = a1
    a[2] = a2

    total = 0
    u = a[1]
    v = a[2]
    l = lca(u, v)
    total += l

    for i in range(2, m + 1):
        a[2 * i - 1] = (x * a[2 * i - 3] + y * a[2 * i - 2] + z) % n
        a[2 * i] = (x * a[2 * i - 2] + y * a[2 * i - 1] + z) % n
        u = (a[2 * i - 1] + l) % n
        v = a[2 * i]
        l = lca(u, v)
        total += l

    print(total)

threading.Thread(target=main).start()
