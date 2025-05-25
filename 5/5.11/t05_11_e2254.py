import sys

def deliver(x, B, k):
    prefix_sum = [0] * (len(x) + 1)
    for i in range(len(x)):
        prefix_sum[i+1] = prefix_sum[i] + x[i]

    for i in range(len(x) - k + 1):
        mid = i + k // 2
        median = x[mid]
        left_count = mid - i
        left_sum = prefix_sum[mid] - prefix_sum[i]
        left_cost = median * left_count - left_sum
        right_count = i + k - 1 - mid
        right_sum = prefix_sum[i + k] - prefix_sum[mid + 1]
        right_cost = right_sum - median * right_count
        total_cost = left_cost + right_cost

        if total_cost <= B:
            return True
    return False

def fields(x, B):
    left, right = 0, len(x)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if deliver(x, B, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

input = sys.stdin.read
data = input().split()

R = int(data[0])
L = int(data[1])
B = int(data[2])
x = list(map(int, data[3:]))

print(fields(x, B))
