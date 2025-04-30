from collections import deque

def burn(n, edges, start):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * (n + 1)
    q = deque()

    for node in start:
        dist[node] = 0
        q.append(node)

    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                q.append(neighbor)

    max_dist = max(dist[1:])
    candidates = [i for i, d in enumerate(dist) if d == max_dist]
    return max_dist, min(candidates)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
start_nodes = list(map(int, input().split()))

time, last_node = burn(n, edges, start_nodes)
print(time)
print(last_node)
