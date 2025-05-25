class Queue:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)
        return "ok"

    def pop(self):
        if not self.empty():
            return self.items.pop(0)
        else:
            return "error"

    def front(self):
        if not self.empty():
            return self.items[0]
        else:
            return "error"

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return "ok"

    def empty(self):
        return len(self.items) == 0

queue = Queue()

while True:
    command = input().split()
    cmd_type = command[0]

    if cmd_type == "push":
        n = int(command[1])
        print(queue.push(n))
    elif cmd_type == "pop":
        print(queue.pop())
    elif cmd_type == "front":
        print(queue.front())
    elif cmd_type == "size":
        print(queue.size())
    elif cmd_type == "clear":
        print(queue.clear())
    elif cmd_type == "exit":
        print("bye")
        break