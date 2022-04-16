from typing import Optional, List

from binary_tree_traversals import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def helper(node):
            nonlocal diameter
            if node:
                l_h = helper(node.left)
                r_h = helper(node.right)
                diameter = max(diameter, l_h + r_h)
                return max(l_h, r_h) + 1
            else:
                return 0

        helper(root)
        return diameter


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    # root_node1.left = TreeNode(2)
    # root_node1.right = TreeNode(3)
    # root_node1.left.left = TreeNode(4)
    # root_node1.left.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(root_node1))
