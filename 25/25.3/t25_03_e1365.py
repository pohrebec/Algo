import heapq

INF = 10**9

def dijkstra(n, s, f, graph):
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        cur_dist, u = heapq.heappop(pq)
        if cur_dist > dist[u]:
            continue
        for v in range(n):
            weight = graph[u][v]
            if weight != -1 and dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return -1 if dist[f] == INF else dist[f]

n, s, f = map(int, input().split())
s -= 1
f -= 1

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

result = dijkstra(n, s, f, graph)
print(result)