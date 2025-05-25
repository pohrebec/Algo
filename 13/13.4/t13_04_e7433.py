A1 = input()
P1 = input()
stack = []
A = int(A1)
P = int(P1)

if A == 0:
    stack.append(0)
else:
    while A > 0:
        remainder = A % P
        stack.append(remainder)
        A //= P

result = []
while stack:
    digit = stack.pop()
    if 0 <= digit <= 9:
        result.append(str(digit))
    else:
        result.append(f"[{digit}]")

print("".join(result))