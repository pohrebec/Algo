import heapq

n, m = map(int, input().split())

def prim(graph, n, banned_edge=None):
    visited = [False] * (n + 1)
    min_heap = []
    edges_used = []
    total_cost = 0
    visited[1] = True

    for (to, cost, idx) in graph[1]:
        if idx != banned_edge:
            heapq.heappush(min_heap, (cost, 1, to, idx))
    count = 1

    while min_heap and count < n:
        cost, u, v, idx = heapq.heappop(min_heap)
        if visited[v]:
            continue
        visited[v] = True
        total_cost += cost
        edges_used.append(idx)
        count += 1
        for (to, c, i) in graph[v]:
            if not visited[to] and i != banned_edge:
                heapq.heappush(min_heap, (c, v, to, i))

    if count == n:
        return total_cost, edges_used
    else:
        return None, None

edges = []
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    graph[a].append((b, c, i))
    graph[b].append((a, c, i))

cost1, mst_edges = prim(graph, n)
cost2 = float('inf')

for e in mst_edges:
    candidate, _ = prim(graph, n, banned_edge=e)
    if candidate is not None and candidate >= cost1:
        cost2 = min(cost2, candidate)

print(cost1, cost2)
