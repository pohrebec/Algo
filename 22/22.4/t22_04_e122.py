def paths(n, edges, a, b, d):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    def dfs(current, target, depth, visited):
        if depth > d:
            return 0
        if current == target and depth > 0:
            return 1
        count = 0
        for neighbor in graph[current]:
            if neighbor not in visited:
                count += dfs(neighbor, target, depth + 1, visited | {neighbor})
        return count

    return dfs(a, b, 0, {a})

n, k, a, b, d = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

print(paths(n, edges, a, b, d))
