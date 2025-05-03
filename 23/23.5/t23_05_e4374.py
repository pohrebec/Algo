import sys
sys.setrecursionlimit(200000)

n, m = map(int, input().split())
edges = []
graph = [[] for _ in range(n + 1)]

for idx in range(1, m + 1):
    a, b = map(int, input().split())
    edges.append((a, b))
    graph[a].append((b, idx))
    graph[b].append((a, idx))

tin = [0] * (n + 1)
low = [0] * (n + 1)
visited = [False] * (n + 1)
bridges = set()
timer = 1

def dfs(v, parent_edge):
    global timer
    visited[v] = True
    tin[v] = low[v] = timer
    timer += 1
    for to, idx in graph[v]:
        if idx == parent_edge:
            continue
        if visited[to]:
            low[v] = min(low[v], tin[to])
        else:
            dfs(to, idx)
            low[v] = min(low[v], low[to])
            if low[to] > tin[v]:
                bridges.add(idx)

dfs(1, -1)

k = int(input())
for _ in range(k):
    parts = list(map(int, input().split()))
    c = parts[0]
    query_edges = parts[1:]
    if any(e in bridges for e in query_edges):
        print("Disconnected")
    else:
        print("Connected")
