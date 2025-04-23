n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

def multi(n, m, edges):
    s = set()
    for u, v in edges:
        if (u, v) in s:
            return "YES"
        s.add((u, v))
    return "NO"

print(multi(n, m, edges))
