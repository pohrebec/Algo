n, m = map(int, input().split())
deg = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1

for i in range(1, n + 1):
    print(deg[i])
