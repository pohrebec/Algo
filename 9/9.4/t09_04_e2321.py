n = int(input())
arr = list(map(int, input().split()))

def sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    l = [x for x in arr if x < pivot]
    m = [x for x in arr if x == pivot]
    r = [x for x in arr if x > pivot]
    return sort(l) + m + sort(r)

sorted_arr = sort(arr)
print(" ".join(map(str, sorted_arr)))