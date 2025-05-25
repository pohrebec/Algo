import math

def f(x):
    return x**3 + x + 1

def find_43():
    left, right = 0.0, 10.0
    eps = 1e-7
    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) > 5:
            right = mid
        else:
            left = mid
    return left
x = find_43()
print(f"{x}")


def f(x):
    return math.sin(x) - x / 3

def find_44():
    left, right = 1.6, 3.0
    eps = 1e-7
    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) * f(left) <= 0:
            right = mid
        else:
            left = mid
    return left
x = find_44()
print(f"{x}")

def f(x):
    return x**3 + 4*x**2 + x - 6

def find_45():
    left, right = 0.0, 2.0
    eps = 1e-7
    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) * f(left) <= 0:
            right = mid
        else:
            left = mid
    return left
x = find_45()
print(f"{x}")

#1.3787966966629028
#2.278862583637238
#0.9999999403953552
