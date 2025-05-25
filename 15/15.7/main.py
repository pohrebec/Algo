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

    def _get_length(self) -> int:
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def _get_node(self, index: int) -> [Node | None]:
        if index < 0:
            return None
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        return current

    def ReorderList(self) -> None:
        if self.head is None or self.head.next is None:
            return

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head1 = self.head
        head2 = slow.next
        slow.next = None
        prev = None
        current = head2

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head2 = prev
        current1 = head1
        current2 = head2

        while current1 and current2:
            next1 = current1.next
            next2 = current2.next
            current1.next = current2

            if next1 is not None:
                current2.next = next1

            current1 = next1
            current2 = next2

        if self.head:
            current = self.head
            while current.next:
                current = current.next
            self.tail = current

    def Print(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    n = int(input())
    if n > 0:
        values = map(int, input().split())
        my_list = List()

        for val in values:
            my_list.addToTail(val)

        my_list.ReorderList()
        my_list.Print()
    else:
        my_list = List()
        my_list.Print()