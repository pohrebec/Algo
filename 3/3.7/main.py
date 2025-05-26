import bisect
import sys

def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    colors = list(map(int, data[1:n+1]))
    m = int(data[n+1])
    queries = list(map(int, data[n+2:]))

    for q in queries:
        left = bisect.bisect_left(colors, q)
        right = bisect.bisect_right(colors, q)
        print(right - left)

main()
