import sys
input = sys.stdin.read
data = input().split()

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.zero = [0] * (4 * self.n)
        self.negative = [0] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, v, tl, tr):
        if tl == tr:
            self.zero[v] = 1 if data[tl] == 0 else 0
            self.negative[v] = 1 if data[tl] < 0 else 0
        else:
            tm = (tl + tr) // 2
            self.build(data, v*2, tl, tm)
            self.build(data, v*2+1, tm+1, tr)
            self.zero[v] = self.zero[v*2] + self.zero[v*2+1]
            self.negative[v] = self.negative[v*2] + self.negative[v*2+1]

    def update(self, v, tl, tr, pos, value):
        if tl == tr:
            self.zero[v] = 1 if value == 0 else 0
            self.negative[v] = 1 if value < 0 else 0
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v*2, tl, tm, pos, value)
            else:
                self.update(v*2+1, tm+1, tr, pos, value)
            self.zero[v] = self.zero[v*2] + self.zero[v*2+1]
            self.negative[v] = self.negative[v*2] + self.negative[v*2+1]

    def query(self, v, tl, tr, l, r):
        if l > r:
            return (0, 0)
        if l == tl and r == tr:
            return (self.zero[v], self.negative[v])
        tm = (tl + tr) // 2
        left = self.query(v*2, tl, tm, l, min(r, tm))
        right = self.query(v*2+1, tm+1, tr, max(l, tm+1), r)
        return (left[0] + right[0], left[1] + right[1])

idx = 0
while idx < len(data):
    n = int(data[idx])
    k = int(data[idx+1])
    idx += 2
    arr = list(map(int, data[idx:idx+n]))
    idx += n

    st = SegmentTree(arr)
    res = []
    for _ in range(k):
        op = data[idx]
        if op == 'C':
            i = int(data[idx+1]) - 1
            v = int(data[idx+2])
            st.update(1, 0, n-1, i, v)
            idx += 3
        else:
            l = int(data[idx+1]) - 1
            r = int(data[idx+2]) - 1
            z, neg = st.query(1, 0, n-1, l, r)
            if z > 0:
                res.append('0')
            else:
                res.append('-' if neg % 2 == 1 else '+')
            idx += 3
    print(''.join(res))