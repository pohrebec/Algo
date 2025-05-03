import sys
sys.setrecursionlimit(200000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
components = []

def dfs(v, comp):
    visited[v] = True
    comp.append(v)
    for to in graph[v]:
        if not visited[to]:
            dfs(to, comp)

for i in range(1, n + 1):
    if not visited[i]:
        comp = []
        dfs(i, comp)
        components.append(comp)

print(len(components))
for comp in components:
    print(len(comp))
    print(*comp)
