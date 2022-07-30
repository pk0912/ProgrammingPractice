from collections import deque

from leetcode.tree.binary_tree_traversals import TreeNode
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def getAllElementsRecursive(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        output = []
        t1 = self.inorderTraversal(root1)
        t2 = self.inorderTraversal(root2)
        i = 0
        j = 0
        while i < len(t1) and j < len(t2):
            if t1[i] < t2[j]:
                output.append(t1[i])
                i += 1
            elif t1[i] > t2[j]:
                output.append(t2[j])
                j += 1
            else:
                output.append(t1[i])
                output.append(t2[j])
                i += 1
                j += 1
        if i < len(t1):
            output += t1[i:]
        if j < len(t2):
            output += t2[j:]
        return output

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        node_stack1 = deque()
        node_stack2 = deque()
        output = []
        while root1 or root2 or node_stack1 or node_stack2:
            while root1:
                node_stack1.appendleft(root1)
                root1 = root1.left
            while root2:
                node_stack2.appendleft(root2)
                root2 = root2.left
            if not node_stack2 or (node_stack1 and node_stack1[0].val < node_stack2[0].val):
                popped_node = node_stack1.popleft()
                root1 = popped_node.right
            else:
                popped_node = node_stack2.popleft()
                root2 = popped_node.right
            output.append(popped_node.val)

        return output


if __name__ == '__main__':
    root_node1 = TreeNode(2)
    root_node1.left = TreeNode(1)
    root_node1.right = TreeNode(4)
    root_node2 = TreeNode(1)
    root_node2.left = TreeNode(0)
    root_node2.right = TreeNode(3)
    print(Solution().getAllElements(root_node1, root_node2))
