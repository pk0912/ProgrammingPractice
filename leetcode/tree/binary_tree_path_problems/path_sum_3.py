from typing import Optional

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path_count = 0

        def helper(node):
            nonlocal path_count
            if node is not None:
                if node.val == targetSum:
                    path_count += 1
                left_sums = helper(node.left)
                right_sums = helper(node.right)
                path_sums = []
                for i in left_sums + right_sums:
                    if node.val + i == targetSum:
                        path_count += 1
                    path_sums.append(node.val + i)
                path_sums.append(node.val)
                return path_sums
            else:
                return []

        helper(root)
        return path_count


if __name__ == '__main__':
    root_node1 = TreeNode(5)
    root_node1.left = TreeNode(4)
    root_node1.right = TreeNode(8)
    root_node1.left.left = TreeNode(11)
    # root_node1.left.right = TreeNode(2)
    root_node1.right.left = TreeNode(13)
    root_node1.right.right = TreeNode(4)
    root_node1.left.left.left = TreeNode(7)
    root_node1.left.left.right = TreeNode(2)
    # root_node1.left.right.right = TreeNode(1)
    root_node1.right.right.left = TreeNode(5)
    root_node1.right.right.right = TreeNode(1)

    print(Solution().pathSum(TreeNode(1), 1))
