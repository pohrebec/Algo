import bisect

def cyclic_binary(n):
    bin_str = bin(n)[2:]
    rotations = []
    curr = bin_str
    length = len(bin_str)

    for _ in range(length):
        val = int(curr, 2)
        rotations.append(val)
        curr = curr[1:] + curr[0]
    rotations.sort()

    max_val = rotations[-1]
    index = bisect.bisect_left(rotations, max_val)
    if index != len(rotations) and rotations[index] == max_val:
        return max_val
    else:
        return -1

n = int(input())
print(cyclic_binary(n))