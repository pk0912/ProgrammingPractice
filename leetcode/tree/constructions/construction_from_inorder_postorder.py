from typing import List, Optional

from leetcode.tree.binary_tree_traversals import TreeNode


"""
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
"""


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_ind = -1
        inorder_val_ind_dict = dict()

        for ind, val in enumerate(inorder):
            inorder_val_ind_dict[val] = ind

        def helper(left, right):
            nonlocal postorder_ind
            if left <= right:
                root_index = inorder_val_ind_dict[postorder[postorder_ind]]
                postorder_ind -= 1
                node = TreeNode(inorder[root_index])
                node.right = helper(root_index + 1, right)
                node.left = helper(left, root_index - 1)
                return node

        return helper(0, len(inorder) - 1)


if __name__ == '__main__':
    root = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(Solution().inorderTraversal(root))
