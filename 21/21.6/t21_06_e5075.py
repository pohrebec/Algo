n, m = map(int, input().split())
u_degree = [0] * (n + 1)
v_degree = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    v_degree[v] += 1
    u_degree[u] += 1

for i in range(1, n + 1):
    print(v_degree[i], u_degree[i])

