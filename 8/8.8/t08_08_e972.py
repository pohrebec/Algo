n = int(input())
times = []

for _ in range(n):
    h, m, s = map(int, input().split())
    times.append((h, m, s))

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if times[j] < times[min_idx]:
            min_idx = j
    times[i], times[min_idx] = times[min_idx], times[i]

for time in times:
    print(time[0], time[1], time[2])
