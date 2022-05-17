from typing import Optional

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None


if __name__ == '__main__':
    root_node1 = TreeNode(5)
    root_node1.left = TreeNode(3)
    root_node1.right = TreeNode(6)
    root_node1.left.left = TreeNode(2)
    root_node1.left.right = TreeNode(4)
    root_node1.right.right = TreeNode(7)
    print(Solution().searchBST(root_node1, 4).val)
