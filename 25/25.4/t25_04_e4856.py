n, m = map(int, input().split())
s, f = map(int, input().split())

def bellman_ford(n, m, s, f, edges):
    INF = float('inf')
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)
    dist[s] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                parent[u] = v
                updated = True
        if not updated:
            break

    if dist[f] == INF:
        print(-1)
        return

    path = []
    current = f
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    print(dist[f])
    print(" ".join(map(str, path)))

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

bellman_ford(n, m, s, f, edges)
