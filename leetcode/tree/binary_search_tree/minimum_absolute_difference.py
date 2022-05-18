import math
from typing import Optional

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mad = math.inf
        prev_val = None

        def helper(node):
            nonlocal mad, prev_val
            if node:
                helper(node.left)
                if prev_val is not None:
                    mad = min(mad, abs(prev_val - node.val))
                prev_val = node.val
                helper(node.right)

        helper(root)

        if mad == math.inf:
            return 0
        return mad


if __name__ == '__main__':
    root_node1 = TreeNode(50)
    root_node1.left = TreeNode(20)
    root_node1.right = TreeNode(60)
    root_node1.left.left = TreeNode(15)
    root_node1.left.right = TreeNode(30)
    root_node1.right.left = TreeNode(55)
    root_node1.right.right = TreeNode(65)
    root_node1.left.left.left = TreeNode(10)
    root_node1.left.left.right = TreeNode(18)
    root_node1.left.left.right.left = TreeNode(16)
    root_node1.left.left.right.right = TreeNode(19)
    print(Solution().getMinimumDifference(root_node1))

    root_node2 = TreeNode(0)
    root_node2.right = TreeNode(2236)
    root_node2.right.left = TreeNode(1277)
    root_node2.right.right = TreeNode(2776)
    root_node2.right.left = TreeNode(519)
    print(Solution().getMinimumDifference(root_node2))
