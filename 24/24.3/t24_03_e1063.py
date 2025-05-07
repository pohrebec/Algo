def count():
    m, n = map(int, input().split())
    grid = [list(input().strip()) for _ in range(m)]
    visited = [[False]*n for _ in range(m)]

    def dfs(x, y):
        stack = [(x, y)]
        while stack:
            i, j = stack.pop()
            if visited[i][j]:
                continue
            visited[i][j] = True
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == '#' and not visited[ni][nj]:
                        stack.append((ni, nj))

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)

count()