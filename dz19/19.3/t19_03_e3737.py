n = int(input())
arr = list(map(int, input().split()))

def heap(arr):
    n = len(arr)
    for i in range(n // 2):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] > arr[l]:
            return "NO"
        if r < n and arr[i] > arr[r]:
            return "NO"
    return "YES"

print(heap(arr))
