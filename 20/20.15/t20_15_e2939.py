class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [None] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, v, tl, tr):
        if tl == tr:
            self.tree[v] = data[tl]
        else:
            tm = (tl + tr) // 2
            self.build(data, v*2, tl, tm)
            self.build(data, v*2+1, tm+1, tr)
            self.tree[v] = self.tree[v*2] + self.tree[v*2+1]

    def push(self, v, tl, tr):
        if self.lazy[v] is not None:
            d = self.lazy[v]
            self.tree[v] = (tr - tl + 1) * d
            if tl != tr:
                self.lazy[v*2] = d
                self.lazy[v*2+1] = d
            self.lazy[v] = None

    def range_update(self, v, tl, tr, l, r, d):
        self.push(v, tl, tr)
        if l > r:
            return
        if l == tl and r == tr:
            self.lazy[v] = d
            self.push(v, tl, tr)
        else:
            tm = (tl + tr) // 2
            self.range_update(v*2, tl, tm, l, min(r, tm), d)
            self.range_update(v*2+1, tm+1, tr, max(l, tm+1), r, d)
            self.tree[v] = self.tree[v*2] + self.tree[v*2+1]

    def range_query(self, v, tl, tr, l, r):
        self.push(v, tl, tr)
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return (
            self.range_query(v*2, tl, tm, l, min(r, tm)) +
            self.range_query(v*2+1, tm+1, tr, max(l, tm+1), r)
        )

n, q = map(int, input().split())
arr = list(map(int, input().split()))
seg_tree = SegmentTree(arr)

for _ in range(q):
    parts = input().split()
    if parts[0] == '=':
        i, j, d = int(parts[1]) - 1, int(parts[2]) - 1, int(parts[3])
        seg_tree.range_update(1, 0, n - 1, i, j, d)
    elif parts[0] == '?':
        f, t = int(parts[1]) - 1, int(parts[2]) - 1
        print(seg_tree.range_query(1, 0, n - 1, f, t))