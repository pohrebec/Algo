class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def insert(self, val):
        self.head = self._insert_rec(self.head, val)

    def _insert_rec(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self._insert_rec(root.left, val)
        else:
            root.right = self._insert_rec(root.right, val)
        return root

    def same_tree(self, other):
        return 1 if self._same_tree_rec(self.head, other.head) else 0

    def _same_tree_rec(self, p1, p2):
        if p1 is None and p2 is None:
            return True
        if p1 is None or p2 is None:
            return False
        if p1.val != p2.val:
            return False
        return (self._same_tree_rec(p1.left, p2.left) and
                self._same_tree_rec(p1.right, p2.right))

if __name__ == "__main__":
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    tree1 = Tree()
    for v in arr1:
        tree1.insert(v)

    tree2 = Tree()
    for v in arr2:
        tree2.insert(v)

    print(tree1.same_tree(tree2))
