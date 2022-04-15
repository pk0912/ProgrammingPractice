from typing import Optional

from binary_tree_traversals import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, level):
            if node:
                return max(helper(node.left, level + 1), helper(node.right, level + 1))
            return level
        return helper(root, 0)


if __name__ == '__main__':
    root_node1 = TreeNode(3)
    # root_node1.left = TreeNode(9)
    root_node1.right = TreeNode(20)
    # root_node1.right.left = TreeNode(15)
    # root_node1.right.right = TreeNode(7)
    print(Solution().maxDepth(root_node1))
