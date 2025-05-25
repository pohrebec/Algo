import math

def find_x(C):
    left = 0.0
    right = max(1.0, C)
    eps = 1e-7

    while right - left > eps:
        mid = (left + right) / 2
        value = mid**2 + math.sqrt(mid)

        if value < C:
            left = mid
        else:
            right = mid

    return left

C = float(input())
x = find_x(C)
print(f"{x}")
