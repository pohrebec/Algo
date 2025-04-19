import math
import sys
input = sys.stdin.read

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(arr, v*2, tl, tm)
            self.build(arr, v*2+1, tm+1, tr)
            self.tree[v] = math.gcd(self.tree[v*2], self.tree[v*2+1])

    def gcd(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left = self.gcd(v*2, tl, tm, l, min(r, tm))
        right = self.gcd(v*2+1, tm+1, tr, max(l, tm+1), r)
        return math.gcd(left, right)

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v*2, tl, tm, pos, new_val)
            else:
                self.update(v*2+1, tm+1, tr, pos, new_val)
            self.tree[v] = math.gcd(self.tree[v*2], self.tree[v*2+1])

def main():
    data = input().split()
    idx = 0

    n = int(data[idx])
    idx += 1
    a = list(map(int, data[idx:idx+n]))
    idx += n
    m = int(data[idx])
    idx += 1

    st = SegmentTree(a)
    output = []

    for _ in range(m):
        q = int(data[idx])
        l = int(data[idx+1]) - 1
        r = int(data[idx+2])
        idx += 3

        if q == 1:
            output.append(str(st.gcd(1, 0, n - 1, l, r - 1)))
        elif q == 2:
            st.update(1, 0, n - 1, l, r)

    print('\n'.join(output))

if __name__ == "__main__":
    main()