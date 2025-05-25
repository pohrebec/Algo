class Stack:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)
        return "ok"

    def pop(self):
        if self.items:
            return self.items.pop()
        return "error"

    def back(self):
        if self.items:
            return self.items[-1]
        return "error"

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        return "ok"

def main():
    stack = Stack()
    while True:
        try:
            command = input().strip()
        except EOFError:
            break

        if command == "exit":
            print("bye")
            break
        elif command.startswith("push"):
            _, n = command.split()
            print(stack.push(int(n)))
        elif command == "pop":
            print(stack.pop())
        elif command == "back":
            print(stack.back())
        elif command == "size":
            print(stack.size())
        elif command == "clear":
            print(stack.clear())

if __name__ == "__main__":
    main()
