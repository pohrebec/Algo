n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    if sum(matrix[i]) == 1:
        cnt += 1

print(cnt)