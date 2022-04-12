from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder(self, node, output):
        if node is not None:
            output.append(node.val)
            self.preorder(node.left, output)
            self.preorder(node.right, output)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.preorder(root, output)
        return output

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def postorder(node):
            if node is not None:
                postorder(node.left)
                postorder(node.right)
                output.append(node.val)

        postorder(root)
        return output

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


if __name__ == '__main__':
    root_node = TreeNode(1)
    root_node.left = TreeNode(2)
    root_node.right = TreeNode(3)
    root_node.left.left = TreeNode(4)
    root_node.left.right = TreeNode(5)
    root_node.right.left = TreeNode(6)
    root_node.right.right = TreeNode(7)
    sol = Solution()
    print(sol.inorderTraversal(root_node))
    print(sol.preorderTraversal(root_node))
    print(sol.postorderTraversal(root_node))
    print(sol.levelOrder(None))
