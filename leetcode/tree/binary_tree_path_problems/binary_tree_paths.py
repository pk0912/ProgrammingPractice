from typing import Optional, List

from leetcode.tree.binary_tree_traversals import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = list()

        def helper(node, path):
            if node is not None:
                if path != "":
                    path += "->"
                if node.left is None and node.right is None:
                    output.append(path + str(node.val))
                else:
                    if node.left:
                        helper(node.left, path + str(node.val))
                    if node.right:
                        helper(node.right, path + str(node.val))

        helper(root, "")
        return output


if __name__ == '__main__':
    root_node1 = TreeNode(1)
    root_node1.left = TreeNode(2)
    root_node1.right = TreeNode(3)
    root_node1.left.right = TreeNode(5)
    print(Solution().binaryTreePaths(root_node1))
