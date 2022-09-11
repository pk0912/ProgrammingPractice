import math
from typing import Optional, List

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        nodes = []

        def helper(node):
            nonlocal prev, nodes
            if node:
                helper(node.left)
                if prev is not None and node.val < prev.val:
                    if len(nodes) == 0:
                        nodes.append(prev)
                    nodes.append(node)
                prev = node
                helper(node.right)

        if root:
            helper(root)
            if len(nodes) > 0:
                nodes[0].val, nodes[-1].val = nodes[-1].val, nodes[0].val


if __name__ == '__main__':
    root_node = TreeNode(1)
    root_node.left = TreeNode(3)
    root_node.left.right = TreeNode(2)
    print(Solution().inorderTraversal(root_node))
    Solution().recoverTree(root_node)
    print(Solution().inorderTraversal(root_node))

    root_node1 = TreeNode(3)
    root_node1.right = TreeNode(2)
    root_node1.right.right = TreeNode(1)
    print(Solution().inorderTraversal(root_node1))
    Solution().recoverTree(root_node1)
    print(Solution().inorderTraversal(root_node1))

    root_node2 = TreeNode(3)
    root_node2.left = TreeNode(1)
    root_node2.right = TreeNode(4)
    root_node2.right.left = TreeNode(2)
    print(Solution().inorderTraversal(root_node2))
    Solution().recoverTree(root_node2)
    print(Solution().inorderTraversal(root_node2))

    root_node3 = TreeNode(2)
    root_node3.left = TreeNode(3)
    root_node3.right = TreeNode(1)
    print(Solution().inorderTraversal(root_node3))
    Solution().recoverTree(root_node3)
    print(Solution().inorderTraversal(root_node3))
