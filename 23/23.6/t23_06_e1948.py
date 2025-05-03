import sys
sys.setrecursionlimit(2 * 10**5)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [0] * (n + 1)
result = []
cycle_found = False

def dfs(v):
    global cycle_found
    visited[v] = 1
    for to in graph[v]:
        if visited[to] == 0:
            dfs(to)
            if cycle_found:
                return
        elif visited[to] == 1:
            cycle_found = True
            return
    visited[v] = 2
    result.append(v)

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        if cycle_found:
            print(-1)
            exit()

print(*reversed(result))
