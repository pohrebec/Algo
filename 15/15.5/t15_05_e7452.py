class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None

class List:
    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def _print_reverse_recursive(self, node: Node | None) -> None:
        if node is None:
            return
        self._print_reverse_recursive(node.next)
        print(node.data, end=" ")

    def PrintReverse(self) -> None:
        self._print_reverse_recursive(self.head)
        print()

if __name__ == "__main__":
    n_str = input()
    n = int(n_str)
    values_str = input()
    values_list_str = values_str.split()
    my_list = List()

    for val_str in values_list_str:
        my_list.addToTail(int(val_str))

    my_list.Print()
    my_list.PrintReverse()