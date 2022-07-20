from collections import deque

from leetcode.tree.binary_tree_traversals import TreeNode
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

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

    def go_to_the_left(self, node, left_tree):
        left_root = node
        if left_tree:
            while node and node.left:
                node = node.left
            node.left = left_tree
        return left_root

    # def go_to_the_right(self, node, right_tree):
    #     if right_tree:
    #         while node and node.right:
    #             node = node.right
    #         node.left = right_tree
    #     return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        parent_node = root
        child_dir = None
        while root is not None:
            if root.val == key:
                if root.left is not None:
                    root.val = root.left.val
                    right_subtree = root.left.right
                    root.left = root.left.left
                    if root.right:
                        root.right = self.go_to_the_left(root.right, right_subtree)
                    else:
                        root.right = right_subtree
                elif root.right is not None:
                    root.val = root.right.val
                    left_subtree = root.right.left
                    root.right = root.right.right
                    root.left = left_subtree
                else:
                    if root == node:
                        node = None
                    if child_dir == "right":
                        parent_node.right = None
                    elif child_dir == "left":
                        parent_node.left = None
                break
            elif root.val < key:
                parent_node = root
                root = root.right
                child_dir = "right"
            else:
                parent_node = root
                root = root.left
                child_dir = "left"
        return node


if __name__ == '__main__':
    root_node1 = TreeNode(50)
    root_node1.left = TreeNode(30)
    root_node1.right = TreeNode(70)
    # root_node1.left.left = TreeNode(7)
    root_node1.left.right = TreeNode(40)
    root_node1.right.left = TreeNode(60)
    root_node1.right.right = TreeNode(80)
    # root_node1.left.left.left = TreeNode(6)
    # root_node1.left.left.right = TreeNode(8)
    # root_node1.left.right.left = TreeNode(13)
    # root_node1.left.right.right = TreeNode(24)
    # root_node1.right.right.left = TreeNode(47)
    # root_node1.right.right.left.left = TreeNode(46)
    # root_node1.right.right.left.right = TreeNode(48)

    print(Solution().levelOrder(root_node1))
    root_node2 = Solution().deleteNode(root_node1, 50)
    print(Solution().levelOrder(root_node2))

    """
    [50,30,70,null,40,60,80]
    50
    """
