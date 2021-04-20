from implementation import Node, inorder, postorder, preorder


inorder_traversal = ["D", "B", "E", "A", "F", "C"]
preorder_traversal = ["A", "B", "D", "E", "C", "F"]


def search_root(inorder_t, root_val):
    return inorder_t.index(root_val)


def build_tree(inorder_t, preorder_t):
    if len(preorder_t) > 0:
        node = Node(preorder_t[0])
        root_index = search_root(inorder_t, preorder_t[0])
        node.left = build_tree(inorder_t[:root_index], preorder_t[1:root_index+1])
        node.right = build_tree(inorder_t[root_index+1:], preorder_t[root_index+1:])
        return node
    else:
        return None


inorder(build_tree(inorder_traversal, preorder_traversal))
print()
postorder(build_tree(inorder_traversal, preorder_traversal))
print()
preorder(build_tree(inorder_traversal, preorder_traversal))
