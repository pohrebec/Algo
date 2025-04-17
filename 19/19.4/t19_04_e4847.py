import heapq
import sys

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}
        self.REMOVED = '<removed>'
        self.counter = 0

    def add(self, id, priority):
        entry = [-priority, id]
        self.entry_finder[id] = entry
        heapq.heappush(self.heap, entry)

    def pop(self):
        while self.heap:
            priority, id = heapq.heappop(self.heap)
            if id != self.REMOVED:
                del self.entry_finder[id]
                print(f"{id} {-priority}")
                return
        raise KeyError("pop from an empty priority queue")

    def change(self, id, new_priority):
        entry = self.entry_finder.pop(id)
        entry[1] = self.REMOVED
        self.add(id, new_priority)

pq = PriorityQueue()

for line in sys.stdin:
    parts = line.strip().split()
    if not parts:
        continue
    command = parts[0]
    if command == 'ADD':
        id = parts[1]
        priority = int(parts[2])
        pq.add(id, priority)
    elif command == 'POP':
        pq.pop()
    elif command == 'CHANGE':
        id = parts[1]
        new_priority = int(parts[2])
        pq.change(id, new_priority)
