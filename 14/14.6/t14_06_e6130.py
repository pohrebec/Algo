class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, n):
        new_node = Node(n)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1
        return "ok"

    def push_back(self, n):
        new_node = Node(n)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self.is_empty():
            return "error"
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            return "error"
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return value

    def front(self):
        if self.is_empty():
            return "error"
        return self.head.value

    def back(self):
        if self.is_empty():
            return "error"
        return self.tail.value

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return "ok"

    def is_empty(self):
        return self.head is None

deque = Deque()

while True:
    command = input().split()
    cmd_type = command[0]

    if cmd_type == "push_front":
        n = int(command[1])
        print(deque.push_front(n))
    elif cmd_type == "push_back":
        n = int(command[1])
        print(deque.push_back(n))
    elif cmd_type == "pop_front":
        print(deque.pop_front())
    elif cmd_type == "pop_back":
        print(deque.pop_back())
    elif cmd_type == "front":
        print(deque.front())
    elif cmd_type == "back":
        print(deque.back())
    elif cmd_type == "size":
        print(deque.size())
    elif cmd_type == "clear":
        print(deque.clear())
    elif cmd_type == "exit":
        print("bye")
        break