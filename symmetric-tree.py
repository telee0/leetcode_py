"""

https://leetcode.com/problems/symmetric-tree/


"""


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def compareTrees(self, tree_left, tree_right):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not tree_left and not tree_right:
            return True

        if tree_left and tree_right:
            if tree_left.val == tree_right.val:
                return self.compareTrees(tree_left.left, tree_right.right) and self.compareTrees(tree_left.right,
                                                                                        tree_right.left)
            else:
                return False
        else:
            return False


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.compareTrees(root.left, root.right)


sol = Solution()
print(sol.inorderTraversal([1,2,2,2,null,2]))