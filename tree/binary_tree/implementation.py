class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node, end=" ")
    inorder(node.right)


def insert(node, val):
    root = node
    if node is None:
        root = Node(val)
        return root
    q = [node]
    while len(q):
        node = q.pop(0)
        if not node.left:
            node.left = Node(val)
            break
        else:
            q.append(node.left)
        if not node.right:
            node.right = Node(val)
            break
        else:
            q.append(node.right)
    return root


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # root = None
    inorder(root)
    root = insert(root, 8)
    print()
    inorder(root)
