from collections import deque
from typing import Optional

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root:
            num_q = deque([root])
            num_set = set()
            while num_q:
                popped_ele = num_q.popleft()
                if k - popped_ele.val in num_set:
                    return True
                num_set.add(popped_ele.val)
                if popped_ele.left:
                    num_q.append(popped_ele.left)
                if popped_ele.right:
                    num_q.append(popped_ele.right)
        return False


if __name__ == '__main__':
    root_node1 = TreeNode(5)
    root_node1.left = TreeNode(3)
    root_node1.right = TreeNode(6)
    root_node1.left.left = TreeNode(2)
    root_node1.left.right = TreeNode(4)
    root_node1.right.right = TreeNode(9)
    print(Solution().findTarget(root_node1, 12))
