from collections import deque

def chess(coord):
    col = ord(coord[0]) - ord('a')
    row = int(coord[1]) - 1
    return row, col

def valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def knight_moves(start, end):
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]

    visited = [[False]*8 for _ in range(8)]
    q = deque()

    sx, sy = chess(start)
    ex, ey = chess(end)

    q.append((sx, sy, 0))
    visited[sx][sy] = True

    while q:
        x, y, d = q.popleft()
        if (x, y) == (ex, ey):
            return d
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if valid(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, d + 1))

try:
    while True:
        line = input().strip()
        if not line:
            continue
        a, b = line.split()
        d = knight_moves(a, b)
        print(f"To get from {a} to {b} takes {d} knight moves.")
except EOFError:
    pass