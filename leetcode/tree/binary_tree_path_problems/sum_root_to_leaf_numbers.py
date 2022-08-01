from typing import Optional

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        def helper(node, num_str):
            nonlocal total_sum
            if node is not None:
                if node.left is None and node.right is None:
                    total_sum += int(num_str + str(node.val))
                else:
                    if node.left is not None:
                        helper(node.left, num_str+str(node.val))
                    if node.right is not None:
                        helper(node.right, num_str+str(node.val))

        helper(root, "")
        return total_sum


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(3)
    print(Solution().sumNumbers(root_node1))
