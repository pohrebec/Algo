N = int(input())

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def insert(self, path_parts):
        if not path_parts:
            return
        head = path_parts[0]
        if head not in self.children:
            self.children[head] = Node(head)
        self.children[head].insert(path_parts[1:])

    def tree(self, depth=0):
        for name in sorted(self.children):
            print(' ' * depth + name)
            self.children[name].tree(depth + 1)

root = Node("")

for _ in range(N):
    path = input().strip().split('\\')
    root.insert(path)

root.tree()
