import sys

class Priority:
    def __init__(self):
        self.heap = []
        self.pos = {}

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos[self.heap[i][1]] = i
        self.pos[self.heap[j][1]] = j

    def up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent][0] < self.heap[i][0]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def down(self, i):
        n = len(self.heap)
        while True:
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and self.heap[l][0] > self.heap[largest][0]:
                largest = l
            if r < n and self.heap[r][0] > self.heap[largest][0]:
                largest = r
            if largest != i:
                self.swap(i, largest)
                i = largest
            else:
                break

    def pop(self):
        top = self.heap[0]
        last = self.heap.pop()
        del self.pos[top[1]]
        if self.heap:
            self.heap[0] = last
            self.pos[last[1]] = 0
            self.down(0)
        return top

    def add(self, id, priority):
        self.heap.append((priority, id))
        idx = len(self.heap) - 1
        self.pos[id] = idx
        self.up(idx)

    def change(self, id, new_priority):
        i = self.pos[id]
        old_priority = self.heap[i][0]
        self.heap[i] = (new_priority, id)
        if new_priority > old_priority:
            self.up(i)
        else:
            self.down(i)

pq = Priority()

for line in sys.stdin:
    parts = line.strip().split()
    if not parts:
        continue
    cmd = parts[0]

    if cmd == 'ADD':
        id = parts[1]
        priority = int(parts[2])
        pq.add(id, priority)

    elif cmd == 'POP':
        id, priority = pq.pop()
        print(f"{priority} {id}")

    elif cmd == 'CHANGE':
        id = parts[1]
        new_priority = int(parts[2])
        pq.change(id, new_priority)