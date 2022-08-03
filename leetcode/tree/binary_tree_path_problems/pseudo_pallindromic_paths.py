from collections import defaultdict
from typing import Optional

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        pseudo_pallindromic_path_count = 0
        val_count_dict = defaultdict(int)

        def helper(node):
            nonlocal pseudo_pallindromic_path_count
            if node is not None:
                val_count_dict[node.val] += 1
                if node.left is None and node.right is None:
                    odd_count = 0
                    for val in val_count_dict.values():
                        if val % 2 != 0:
                            odd_count += 1
                        if odd_count > 1:
                            break
                    if odd_count <= 1:
                        pseudo_pallindromic_path_count += 1
                else:
                    if node.left is not None:
                        helper(node.left)
                    if node.right is not None:
                        helper(node.right)
                val_count_dict[node.val] -= 1

        helper(root)
        return pseudo_pallindromic_path_count


if __name__ == '__main__':
    root_node1 = TreeNode(2)
    root_node1.left = TreeNode(3)
    root_node1.right = TreeNode(1)
    root_node1.left.left = TreeNode(3)
    root_node1.left.right = TreeNode(1)
    root_node1.right.right = TreeNode(1)
    print(Solution().pseudoPalindromicPaths(root_node1))
