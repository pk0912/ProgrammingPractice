from typing import Optional

from binary_tree_traversals import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node, level):
            if node:
                l_h, is_l_balanced = helper(node.left, level + 1)
                if is_l_balanced:
                    r_h, is_r_balanced = helper(node.right, level + 1)
                    if is_r_balanced:
                        return max(l_h, r_h), abs(r_h - l_h) < 2
                return None, False
            return level, True

        return helper(root, 0)[-1]


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(2)
    root_node1.left.left = TreeNode(3)
    root_node1.left.left.left = TreeNode(4)
    # root_node1.right.right = TreeNode(3)
    # root_node1.right.right.right = TreeNode(4)
    print(Solution().isBalanced(root_node1))
