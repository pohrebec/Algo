from math import log2, ceil, gcd

def lcm(a, b):
    return a * b // gcd(a, b) if a and b else 0

class SegmentTree:

    def __init__(self, array, op, neutral):
        self.k = len(array)
        self.p = ceil(log2(self.k))
        self.n = 2 ** self.p
        self.op = op
        self.neutral = neutral
        self._items = [neutral] * (2 * self.n)

        for i in range(self.k):
            self._items[self.n + i] = array[i]

        for i in range(self.n - 1, 0, -1):
            self._items[i] = op(self._items[2 * i], self._items[2 * i + 1])

    def query(self, a, b):
        res = self.neutral
        left = a + self.n
        right = b + self.n

        while left <= right:
            if left % 2 == 1:
                res = self.op(res, self._items[left])
                left += 1
            if right % 2 == 0:
                res = self.op(res, self._items[right])
                right -= 1
            left //= 2
            right //= 2

        return res

    def update(self, i, value):
        i += self.n
        self._items[i] = value
        i //= 2
        while i > 0:
            self._items[i] = self.op(self._items[2 * i], self._items[2 * i + 1])
            i //= 2

if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        m = int(f.readline())
        queries = [tuple(map(int, f.readline().split())) for _ in range(m)]

    gcd_tree = SegmentTree(arr, gcd, 0)
    lcm_tree = SegmentTree(arr, lcm, 1)

    for q in queries:
        if q[0] == 1:
            _, l, r = q
            g = gcd_tree.query(l - 1, r - 1)
            l_ = lcm_tree.query(l - 1, r - 1)
            if g < l_:
                print("wins")
            elif g > l_:
                print("loser")
            else:
                print("draw")
        else:
            _, i, val = q
            gcd_tree.update(i - 1, val)
            lcm_tree.update(i - 1, val)