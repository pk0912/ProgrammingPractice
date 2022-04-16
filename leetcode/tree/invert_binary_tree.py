from typing import Optional, List

from binary_tree_traversals import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if node:
                node.left, node.right = helper(node.right), helper(node.left)
                return node

        helper(root)
        return root


if __name__ == '__main__':
    root_node1 = TreeNode(4)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(7)
    root_node1.left.left = TreeNode(1)
    root_node1.left.right = TreeNode(3)
    root_node1.right.left = TreeNode(6)
    root_node1.right.right = TreeNode(9)
    sol = Solution()
    root = sol.invertTree(root_node1)
    print(sol.preorderTraversal(root))
