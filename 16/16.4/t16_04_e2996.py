import sys
sys.setrecursionlimit(10**7)
N = int(input())

def dfs(i):
    if cost[i] != -1:
        return cost[i]

    if not sub[i]:
        cost[i] = bribes[i]
        return cost[i]

    sub_cost = min(dfs(s) for s in sub[i])
    cost[i] = bribes[i] + sub_cost
    return cost[i]

bribes = [0] * (N+1)
sub = [[] for _ in range(N+1)]
cost = [-1] * (N+1)

for i in range(1, N+1):
    data = list(map(int, input().split()))
    bribes[i] = data[0]
    k = data[1]
    if k > 0:
        sub[i] = data[2:]

print(dfs(1))