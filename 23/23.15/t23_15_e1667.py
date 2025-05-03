import sys
sys.setrecursionlimit(2 * 10**5)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
rev_graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    rev_graph[v - 1].append(u - 1)

visited = [False] * n
order = []

def dfs1(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs1(v)
    order.append(u)

def dfs2(u, label):
    component[u] = label
    for v in rev_graph[u]:
        if component[v] == -1:
            dfs2(v, label)

for i in range(n):
    if not visited[i]:
        dfs1(i)

component = [-1] * n
label = 0
for u in reversed(order):
    if component[u] == -1:
        dfs2(u, label)
        label += 1

print(label)
print(' '.join(str(component[i] + 1) for i in range(n)))