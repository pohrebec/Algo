n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

def graph(n, m, edges):
    edge_set = set()
    for u, v in edges:
        edge_set.add((min(u, v), max(u, v)))
    return "YES" if len(edge_set) == n * (n - 1) // 2 else "NO"

print(graph(n, m, edges))
