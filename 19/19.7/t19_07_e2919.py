import sys
import heapq

sys.setrecursionlimit(2 * 10**5)

def node(n, children):
    left = [-1] * (n + 1)
    right = [-1] * (n + 1)
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        l, r = children[i - 1]
        left[i] = l
        right[i] = r
        if l != -1:
            parent[l] = i
        if r != -1:
            parent[r] = i

    root = next(i for i in range(1, n + 1) if parent[i] == 0)
    potential = [None] * (n + 1)

    def dfs(u):
        l = left[u]
        r = right[u]

        if l != -1:
            dfs(l)
        if r != -1:
            dfs(r)

        if l == -1 or r == -1:
            potential[u] = 0
        else:
            heapq.heappush(min_heap, (potential[l], l))
            heapq.heappush(min_heap, (potential[r], r))

            potential[u] = 1 + min(potential[l], potential[r])

    min_heap = []
    dfs(root)

    for i in range(1, n + 1):
        l = left[i]
        r = right[i]

        if r != -1 and l == -1:
            return i
        if l != -1 and r != -1 and potential[l] < potential[r]:
            return i

    return -1

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    children = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(node(n, children))
