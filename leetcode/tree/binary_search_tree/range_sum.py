from leetcode.tree.binary_tree_traversals import TreeNode
from typing import Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0

        def helper(node):
            nonlocal range_sum
            if node:
                if low <= node.val <= high:
                    range_sum += node.val
                if node.val > low:
                    helper(node.left)
                if node.val < high:
                    helper(node.right)

        helper(root)
        return range_sum


if __name__ == '__main__':
    root_node1 = TreeNode(10)
    root_node1.left = TreeNode(5)
    root_node1.right = TreeNode(15)
    root_node1.left.left = TreeNode(3)
    root_node1.left.right = TreeNode(7)
    root_node1.right.left = TreeNode(13)
    root_node1.right.right = TreeNode(18)
    root_node1.left.left.left = TreeNode(1)
    root_node1.left.right.left = TreeNode(6)
    print(Solution().rangeSumBST(root_node1, 6, 10))
