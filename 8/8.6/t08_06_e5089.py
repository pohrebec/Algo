n = int(input())
words = [input().strip() for _ in range(n)]

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if words[j] < words[min_idx]:
            min_idx = j
    if min_idx != i:
        words[i], words[min_idx] = words[min_idx], words[i]

for word in words:
    print(word)