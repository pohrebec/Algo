import bisect
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    collection = list(map(int, data[1:n+1]))
    m = int(data[n+1])
    queries = list(map(int, data[n+2:]))

    for k in queries:
        index = bisect.bisect_left(collection, k)
        if index < len(collection) and collection[index] == k:
            print("YES")
        else:
            print("NO")

main()
