from typing import Optional

from binary_tree_traversals import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node:
                l_h = helper(node.left)
                r_h = helper(node.right)
                if l_h == 0:
                    return r_h + 1
                elif r_h == 0:
                    return l_h + 1
                else:
                    return min(l_h, r_h) + 1
            else:
                return 0

        return helper(root)


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    # root_node1.left = TreeNode(2)
    # root_node1.left.left = TreeNode(4)
    root_node1.right = TreeNode(3)
    # root_node1.right.left = TreeNode(5)
    root_node1.right.right = TreeNode(6)
    root_node1.right.right.right = TreeNode(7)
    root_node1.right.right.right.right = TreeNode(8)
    print(Solution().minDepth(root_node1))
