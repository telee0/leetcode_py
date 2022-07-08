"""

https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        memory = []

        node, height = root, 1
        h_min, h_max = (5000, 1)  # if root.left and root.right else (1, 1)

        while node:
            is_leaf = True
            if node.left:
                memory.append([node.left, height+1])
                is_leaf = False
            if node.right:
                memory.append([node.right, height+1])
                is_leaf = False
            if is_leaf:
                if h_max < height:
                    h_max = height
                if h_min > height:
                    h_min = height
                if h_max - h_min > 1:
                    return False
            if len(memory) > 0:
                node, height = memory.pop()
            else:
                break

        return True


sol = Solution()
print(sol.isBalanced([1, null, 2, null, 3]))

