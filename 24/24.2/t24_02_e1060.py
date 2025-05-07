from collections import deque

def maze():
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start = end = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j] == 'X':
                end = (i, j)

    queue = deque([start])
    visited = [[False]*n for _ in range(n)]
    prev = [[None]*n for _ in range(n)]
    visited[start[0]][start[1]] = True

    found = False
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            found = True
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] in ['.', 'X']:
                    visited[nx][ny] = True
                    prev[nx][ny] = (x, y)
                    queue.append((nx, ny))

    if not found:
        print("N")
        return

    x, y = end
    while (x, y) != start:
        if grid[x][y] != '@':
            grid[x][y] = '+'
        x, y = prev[x][y]

    print("Y")
    for row in grid:
        print(''.join(row))

maze()
