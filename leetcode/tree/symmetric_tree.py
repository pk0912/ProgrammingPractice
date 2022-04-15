from typing import Optional

from binary_tree_traversals import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def inorder(node1, node2):
            if node1 and node2:
                if node1.val == node2.val:
                    return inorder(node1.left, node2.right) and inorder(node1.right, node2.left)
                else:
                    return False
            elif node1 or node2:
                return False
            else:
                return True
        return inorder(root, root)


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(2)
    root_node1.left.left = TreeNode(2)
    # root_node1.left.right = TreeNode(3)
    root_node1.right.left = TreeNode(2)
    # root_node1.right.right = TreeNode(3)
    print(Solution().isSymmetric(root_node1))
