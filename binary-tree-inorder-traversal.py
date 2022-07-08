"""

https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        path = []
        path += self.inorderTraversal(root.left)
        path.append(root.val)
        path += self.inorderTraversal(root.right)

        return path

        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []