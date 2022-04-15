from typing import Optional

from binary_tree_traversals import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(node1, node2):
            if node1 and node2:
                if node1.val == node2.val:
                    return inorder(node1.left, node2.left) and inorder(node1.right, node2.right)
                return False
            elif node1 or node2:
                return False
            else:
                return True
        return inorder(p, q)


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(3)
    root_node2 = TreeNode(1)
    root_node2.left = TreeNode(2)
    root_node2.right = TreeNode(3)
    print(Solution().isSameTree(root_node1, root_node2))
