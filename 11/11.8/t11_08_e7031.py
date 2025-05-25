def inversions(xn, t):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        l, inv_l = merge_sort(arr[:mid])
        r, inv_r = merge_sort(arr[mid:])
        merged, cross_inv = merge_count(l, r)
        return merged, inv_l + inv_r + cross_inv

    def merge_count(left, right):
        count = 0
        j = 0
        for x in left:
            while j < len(right) and x > right[j] + t:
                j += 1
            count += j
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count

    _, total_count = merge_sort(xn)
    return total_count

def main():
    with open("input.txt", "r") as f:
        n_t = f.readline().strip()
        arr_line = f.readline().strip()

    n, t = map(int, n_t.split())
    xn = list(map(int, arr_line.split()))

    result = inversions(xn, t)

    with open("output.txt", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()