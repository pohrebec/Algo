N = int(input())
numbers = input().split()

class HashTable:
    def __init__(self, size=200000):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return int(key) % self.size

    def add(self, key):
        h = self._hash(key)
        for k in self.table[h]:
            if k == key:
                return
        self.table[h].append(key)
        self.count += 1

    def size_set(self):
        return self.count

ht = HashTable()

for num in numbers:
    ht.add(num)
print(ht.size_set())
