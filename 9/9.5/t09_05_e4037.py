import sys
sys.setrecursionlimit(200000)
n = int(sys.stdin.readline())
robots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

def merge_sort(arr, temp, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, temp, left, mid)
    merge_sort(arr, temp, mid + 1, right)
    merge(arr, temp, left, mid, right)

def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i][0] <= arr[j][0]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for l in range(left, right + 1):
        arr[l] = temp[l]


temp = [None] * n
merge_sort(robots, temp, 0, n - 1)
for main, aux in robots:
    print(main, aux)
