from typing import Optional

from binary_tree_traversals import TreeNode


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0

        def helper(node):
            nonlocal tilt
            if node:
                l_sum = helper(node.left)
                r_sum = helper(node.right)
                tilt += abs(l_sum - r_sum)
                return l_sum + r_sum + node.val
            else:
                return 0

        helper(root)

        return tilt


if __name__ == '__main__':
    root_node1 = TreeNode(4)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(9)
    root_node1.left.left = TreeNode(3)
    root_node1.left.right = TreeNode(5)
    root_node1.right.right = TreeNode(7)
    print(Solution().findTilt(root_node1))