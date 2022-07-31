from typing import Optional, List

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List:
        output = []

        def helper(node, node_vals):
            if node is not None:
                if node.left is None and node.right is None:
                    node_vals.append(node.val)
                    if sum(node_vals) == targetSum:
                        output.append(node_vals)
                else:
                    if node.left is not None:
                        helper(node.left, node_vals + [node.val])
                    if node.right is not None:
                        helper(node.right, node_vals + [node.val])

        helper(root, [])
        return output


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(3)
    # root_node1.left.left = TreeNode(11)
    # root_node1.right.left = TreeNode(13)
    # root_node1.right.right = TreeNode(4)
    # root_node1.left.left.left = TreeNode(7)
    # root_node1.left.left.right = TreeNode(2)
    # root_node1.right.right.left = TreeNode(5)
    # root_node1.right.right.right = TreeNode(1)
    print(Solution().pathSum(root_node1, 5))
