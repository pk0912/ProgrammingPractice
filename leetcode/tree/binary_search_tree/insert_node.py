from leetcode.tree.binary_tree_traversals import TreeNode
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        direction = None
        new_node = TreeNode(val)
        if root is None:
            return new_node
        while root is not None:
            if root.val < val:
                if root.right is not None:
                    root = root.right
                else:
                    direction = "r"
                    break
            else:
                if root.left is not None:
                    root = root.left
                else:
                    direction = "l"
                    break

        if direction == "l":
            root.left = new_node
        else:
            root.right = new_node
        return node

    # This is faster
    def insertIntoBSTRecursively(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBSTRecursively(root.right, val)
        else:
            root.left = self.insertIntoBSTRecursively(root.left, val)
        return root


if __name__ == '__main__':
    root_node1 = TreeNode(4)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(7)
    root_node1.left.left = TreeNode(1)
    root_node1.left.right = TreeNode(3)
    # root_node1.right.left = TreeNode(60)
    # root_node1.right.right = TreeNode(80)
    # root_node1.left.left.left = TreeNode(6)
    # root_node1.left.left.right = TreeNode(8)
    # root_node1.left.right.left = TreeNode(13)
    # root_node1.left.right.right = TreeNode(24)
    # root_node1.right.right.left = TreeNode(47)
    # root_node1.right.right.left.left = TreeNode(46)
    # root_node1.right.right.left.right = TreeNode(48)

    print(Solution().inorderTraversal(root_node1))
    root_node2 = Solution().insertIntoBSTRecursively(root_node1, 5)
    print(Solution().inorderTraversal(root_node2))
    root_node3 = Solution().insertIntoBSTRecursively(root_node2, 6)
    print(Solution().inorderTraversal(root_node3))
