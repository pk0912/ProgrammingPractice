from typing import Optional

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_sum = float('-inf')

        def helper(node):
            nonlocal max_sum
            if node is not None:
                left_val = helper(node.left)
                right_val = helper(node.right)
                max_sum = max(left_val + node.val + right_val, node.val, node.val + left_val, node.val + right_val, max_sum)
                return max(left_val + node.val, right_val + node.val, node.val)
            else:
                return 0

        helper(root)
        return int(max_sum)


if __name__ == '__main__':
    root_node1 = TreeNode(9)
    root_node1.left = TreeNode(6)
    root_node1.right = TreeNode(-3)
    root_node1.right.left = TreeNode(-6)
    root_node1.right.right = TreeNode(2)
    root_node1.right.right.left = TreeNode(2)
    root_node1.right.right.left.left = TreeNode(-6)
    root_node1.right.right.left.right = TreeNode(-6)
    root_node1.right.right.left.left.left = TreeNode(-6)
    print(Solution().maxPathSum(root_node1))
