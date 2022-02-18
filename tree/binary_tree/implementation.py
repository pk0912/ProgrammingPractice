from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"


def inorder_without_recursion(node):
    stack = deque()
    while node is not None or len(stack) != 0:
        if node is not None:
            stack.appendleft(node)
            node = node.left
        else:
            popped_item = stack.popleft()
            print(popped_item.data, end=" ")
            node = popped_item.right


def inorder_with_recursion(node):
    if node is None:
        return
    inorder(node.left)
    print(node, end=" ")
    inorder(node.right)


def inorder(node, recursion=True):
    if recursion:
        inorder_with_recursion(node)
    else:
        inorder_without_recursion(node)


def preorder(node):
    if node is None:
        return
    print(node, end=" ")
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node, end=" ")


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


def lvl_order_traversal(root):
    final_output = []
    lvl_output = []
    queue = deque([root, "$"])
    while len(queue) > 0:
        first_in_queue = queue.popleft()
        if first_in_queue != "$":
            lvl_output.append(first_in_queue.data)
            if first_in_queue.left:
                queue.append(first_in_queue.left)
            if first_in_queue.right:
                queue.append(first_in_queue.right)
        else:
            if len(queue) == 0:
                break
            else:
                queue.append("$")
                final_output.append(lvl_output)
                lvl_output = []
    if len(lvl_output) != 0:
        final_output.append(lvl_output)
    return final_output


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # root = None
    print("Level Order Traversal : ", end="")
    print(lvl_order_traversal(root))
    print("Inorder using recursion : ", end="")
    inorder(root)
    print()
    print("Inorder without recursion : ", end="")
    inorder(root, recursion=False)
    print()
    root = insert(root, 8)
    print("Inorder using recursion : ", end="")
    inorder(root)
    print()
    print("Inorder without recursion : ", end="")
    inorder(root, recursion=False)
    print()
    print("Preorder : ", end="")
    preorder(root)
    print()
    print("Postorder : ", end="")
    postorder(root)
    print()
