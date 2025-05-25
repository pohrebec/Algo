def karatsuba(x: str, y: str) -> str:
    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))

    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    n = max_len
    m = n // 2
    x1, x0 = x[:-m], x[-m:]
    y1, y0 = y[:-m], y[-m:]
    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    sum_x1x0 = str(int(x1) + int(x0))
    sum_y1y0 = str(int(y1) + int(y0))
    z1 = karatsuba(sum_x1x0, sum_y1y0)
    z1 = str(int(z1) - int(z2) - int(z0))
    result = int(z2) * 10**(2 * m) + int(z1) * 10**m + int(z0)
    return str(result)

def main():
    with open("input.txt", "r") as f:
        A, B = f.read().strip().split()

    if A == "0" or B == "0":
        result = "0"
    else:
        result = karatsuba(A, B)

    with open("output.txt", "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()
