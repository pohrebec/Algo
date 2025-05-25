import heapq
import sys
import math

input = sys.stdin.read
data = input().split()

def prim(points):
    n = len(points)
    used = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    pq = [(0, 0)]
    total = 0

    while pq:
        cost, u = heapq.heappop(pq)
        if used[u]:
            continue
        used[u] = True
        total += cost
        for v in range(n):
            if not used[v]:
                dist = math.hypot(points[u][0] - points[v][0], points[u][1] - points[v][1])
                if dist < min_edge[v]:
                    min_edge[v] = dist
                    heapq.heappush(pq, (dist, v))

    return total

idx = 0
results = []

while True:
    n = int(data[idx])
    idx += 1
    if n == 0:
        break
    points = []
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        points.append((x, y))
        idx += 2
    result = prim(points)
    results.append(f"{result:.2f}")

print("\n".join(results))
