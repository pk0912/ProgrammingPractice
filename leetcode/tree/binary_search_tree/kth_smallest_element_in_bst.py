from collections import deque

from leetcode.tree.binary_tree_traversals import TreeNode
from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        node_stack = deque()
        while (root is not None or len(node_stack) != 0) and len(output) < k:
            if root is not None:
                node_stack.appendleft(root)
                root = root.left
            else:
                popped_ele = node_stack.popleft()
                output.append(popped_ele.val)
                root = popped_ele.right
        return output[-1]


if __name__ == '__main__':
    root_node1 = TreeNode(5)
    root_node1.left = TreeNode(3)
    root_node1.right = TreeNode(6)
    root_node1.left.left = TreeNode(2)
    root_node1.left.left.left = TreeNode(1)
    print(Solution().kthSmallest(root_node1, 500))
