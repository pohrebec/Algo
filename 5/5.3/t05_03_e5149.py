import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
k = int(data[1])
stab = list(map(int, data[2:]))

def cows(stab, k, dist):
    count = 1
    last = stab[0]

    for i in range(1, len(stab)):
        if stab[i] - last >= dist:
            count += 1
            last = stab[i]
            if count == k:
                return True
    return False

def dist(stab, k):
    left = 1
    right = stab[-1] - stab[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if cows(stab, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

print(dist(stab, k))
