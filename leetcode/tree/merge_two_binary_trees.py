from typing import Optional, List

from binary_tree_traversals import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node1, node2):
            if node1 and node2:
                node2.val = node1.val + node2.val
                node2.left = helper(node1.left, node2.left)
                node2.right = helper(node1.right, node2.right)
                return node2
            elif not node2:
                return node1
            else:
                return node2
        return helper(root1, root2)


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    root_node1.left = TreeNode(3)
    root_node1.right = TreeNode(2)
    # root_node1.left.left = TreeNode(5)
    root_node2 = TreeNode(2)
    root_node2.left = TreeNode(1)
    root_node2.right = TreeNode(3)
    root_node2.left.right = TreeNode(4)
    root_node2.right.right = TreeNode(7)
    sol = Solution()
    root = sol.mergeTrees(root_node1, root_node2)
    print(sol.preorderTraversal(root))
