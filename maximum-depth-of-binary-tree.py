# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        paths = [(root, 1)]

        i = 0
        n = 1
        max_depth = 1

        while i < n:
            (node, depth) = paths[i]
            if node.left:
                paths.append((node.left, depth + 1))
                n += 1
            if node.right:
                paths.append((node.right, depth + 1))
                n += 1
            if depth > max_depth:
                max_depth = depth
            i += 1

        return max_depth

sol = Solution()

print(sol.maxDepth([3,9,20,null,null,15,7]))