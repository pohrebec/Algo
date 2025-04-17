import heapq
import sys

input = sys.stdin.read

def process(visitors):
    visitors.sort()
    heap = []
    time = 0
    total_anger = 0
    i = 0
    n = len(visitors)

    while i < n or heap:
        if not heap:
            time = max(time, visitors[i][0])

        while i < n and visitors[i][0] <= time:
            r, w = visitors[i]
            heapq.heappush(heap, (-w, r))
            i += 1

        w_neg, r = heapq.heappop(heap)
        w = -w_neg
        total_anger += (time - r) * w
        time += 1

    return total_anger

def main():
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        visitors = []
        for _ in range(n):
            r = int(data[index])
            w = int(data[index + 1])
            visitors.append((r, w))
            index += 2
        results.append(process(visitors))

    for res in results:
        print(res)

main()