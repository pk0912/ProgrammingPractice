from typing import Optional

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, node_sum):
            if node is not None:
                if node.left is None and node.right is None:
                    return node_sum + node.val == targetSum
                else:
                    left_sum_chk = helper(node.left, node_sum + node.val)
                    if left_sum_chk:
                        return True
                    else:
                        return helper(node.right, node_sum + node.val)

        return helper(root, 0)


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(3)
    # root_node1.left.left = TreeNode(11)
    # root_node1.right.left = TreeNode(13)
    # root_node1.right.right = TreeNode(4)
    # root_node1.left.left.left = TreeNode(7)
    # root_node1.left.left.right = TreeNode(2)
    # root_node1.right.right.right = TreeNode(1)
    print(Solution().hasPathSum(root_node1, 22))
