from typing import List, Optional

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_val_index_dict = dict()

        for ind, val in enumerate(inorder):
            inorder_val_index_dict[val] = ind

        def helper(left, right):
            nonlocal preorder_ind
            if left > right:
                return None
            root_index = inorder_val_index_dict[preorder[preorder_ind]]
            node = TreeNode(inorder[root_index])
            preorder_ind += 1
            node.left = helper(left, root_index - 1)
            node.right = helper(root_index + 1, right)
            return node

        preorder_ind = 0
        return helper(0, len(preorder) - 1)


if __name__ == '__main__':
    root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(Solution().inorderTraversal(root))
