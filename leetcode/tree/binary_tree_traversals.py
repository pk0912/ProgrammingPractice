"""
TODO: Learn about Morris Traversal for inorder,preorder,postorder traversal without recursion in O(1) space and O(n) time
"""


from collections import deque, defaultdict
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

    def preorderTraversalWithoutRecursion(self, root: Optional[TreeNode]) -> List[int]:
        """
        (root, left, right)
        Go to the leftmost leaf node first while putting all visited nodes in the stack
        and also printing out all the nodes that are getting visited.
        When leftmost leaf node is reached,
        pop the current element from the stack and
        shift the node pointer to the right part of this node.
        Repeat the same process again i.e.
        going to the leftmost part while printing out these nodes
        and shifting node pointer to the right subtree when the leftmost part is reached.
        """
        output = []
        node_stack = deque()
        while root is not None or len(node_stack) != 0:
            if root is not None:
                output.append(root.val)
                node_stack.appendleft(root)
                root = root.left
            else:
                popped_ele = node_stack.popleft()
                root = popped_ele.right
        return output

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def inorderTraversalWithoutRecursion(self, root: Optional[TreeNode]) -> List[int]:
        """
        (left, root, right)
        Go to the leftmost leaf node first while putting all visited nodes in the stack.
        When leftmost leaf node is reached focus on the subtree with this node as the root.
        This node has no further left child, so pop it out of the stack and print it out and
        then shift the node pointer to the right part of this node.
        Repeat the same process again i.e.
        going to the leftmost part and then printing it out
        and shifting node pointer to the right subtree when the leftmost part is reached.
        """
        output = []
        node_stack = deque()
        while root is not None or len(node_stack) != 0:
            if root is not None:
                node_stack.appendleft(root)
                root = root.left
            else:
                popped_ele = node_stack.popleft()
                output.append(popped_ele.val)
                root = popped_ele.right
        return output

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def postorder(node):
            if node is not None:
                postorder(node.left)
                postorder(node.right)
                output.append(node.val)

        postorder(root)
        return output

    def postorderTraversalWithoutRecursion(self, root: Optional[TreeNode]) -> List[int]:
        """
        (left, root, right)
        Go to the leftmost leaf node first while putting all visited nodes in the stack.
        When leftmost leaf node is reached focus on the subtree with this node as the root.
        This node has no further left child, so pop it out and
        then check if this element has any right child or not.
        If it does not then that means inorder to print postorder traversal for the subtree with this node as root
        has no left or right child, that means in traversal,
        only this node value is going to be printed for this subtree. So print this value out.
        If it has right child then that means first we have to visit the right subtree in similar fashion
        i.e. going to the leftmost part of this right subtree.
        So we will shift the node pointer to the right subtree of this popped node.
        But we will need this popped node later as well because this is the root node for the subtree in consideration
        and for postorder traversal root node is printed last.
        So we will again put this node into the stack so that it can be visited again.
        But we need to first make the right subtree of this node as None before pushing it back into stack
        else we will get caught in infinite loop as this node will be visited once again
        when the right subtree of this node is traversed.
        Repeat the same process again i.e.
        going to the leftmost part and then printing it out
        and shifting node pointer to the right subtree when the leftmost part is reached.
        """
        output = []
        node_stack = deque()
        while root is not None or len(node_stack) != 0:
            if root is not None:
                node_stack.appendleft(root)
                root = root.left
            else:
                popped_ele = node_stack.popleft()
                if popped_ele.right:
                    root = popped_ele.right
                    popped_ele.right = None
                    node_stack.appendleft(popped_ele)
                else:
                    output.append(popped_ele.val)
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

    def levelOrderWithRecursion(self, root: Optional[TreeNode]) -> List[List[int]]:
        output_dict = defaultdict(list)

        def helper(node, key):
            if node:
                output_dict[key].append(node.val)
                helper(node.left, key + 1)
                helper(node.right, key + 1)

        helper(root, 0)

        return [output_dict[k] for k in sorted(output_dict.keys())]

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        lvl_traversal = []
        switch = False
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
                        if switch:
                            lvl_traversal.reverse()
                        output.append(lvl_traversal)
                        lvl_traversal = []
                        switch = not switch
        return output

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        output.reverse()
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
    print(sol.levelOrder(root_node))
    print(sol.levelOrderWithRecursion(root_node))
    print(sol.zigzagLevelOrder(root_node))
    print(sol.levelOrderBottom(root_node))
    print(sol.inorderTraversal(root_node))
    print(sol.inorderTraversalWithoutRecursion(root_node))
    print(sol.preorderTraversal(root_node))
    print(sol.preorderTraversalWithoutRecursion(root_node))
    print(sol.postorderTraversal(root_node))
    print(sol.postorderTraversalWithoutRecursion(root_node))
