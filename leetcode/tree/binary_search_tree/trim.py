from collections import deque

from leetcode.tree.binary_tree_traversals import TreeNode
from typing import Optional, List


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        lvl_traversal = []
        if root:
            queue = deque([root, "$"])
            while len(queue) > 0:
                popped_ele = queue.popleft()
                if popped_ele != "$":
                    if popped_ele.left:
                        queue.append(popped_ele.left)
                    if popped_ele.right:
                        queue.append(popped_ele.right)
                    lvl_traversal.append(popped_ele.val)
                else:
                    if len(lvl_traversal) > 0:
                        queue.append("$")
                        output.append(lvl_traversal)
                        lvl_traversal = []
        return output

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        node = root
        parent_node = root
        while root is not None:
            if root.val < low:
                if root == node:
                    node = root.right
                else:
                    parent_node.left = root.right
                    root = root.right
            else:
                parent_node = root
                root = root.left
        root = node
        parent_node = node
        while root is not None:
            if root.val > high:
                if root == node:
                    node = root.left
                else:
                    parent_node.right = root.left
                    root = root.left
            else:
                parent_node = root
                root = root.right
        return node


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(2)
    # root_node1.left.left = TreeNode(7)
    # root_node1.left.right = TreeNode(2)
    # root_node1.right.left = TreeNode(60)
    # root_node1.right.right = TreeNode(80)
    # root_node1.left.left.left = TreeNode(6)
    # root_node1.left.left.right = TreeNode(8)
    # root_node1.left.right.left = TreeNode(1)
    # root_node1.left.right.right = TreeNode(24)
    # root_node1.right.right.left = TreeNode(47)
    # root_node1.right.right.left.left = TreeNode(46)
    # root_node1.right.right.left.right = TreeNode(48)

    print(Solution().levelOrder(root_node1))
    root_node2 = Solution().trimBST(root_node1, 2, 4)
    print(Solution().levelOrder(root_node2))
