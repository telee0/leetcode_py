"""

https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        node, depth = root, 1
        memory = []
        while node:
            if node.left is None and node.right is None:
                return depth
            else:
                if node.left:
                    memory.append([node.left, depth + 1])
                if node.right:
                    memory.append([node.right, depth + 1])
                depth += 1
            if len(memory) > 0:
                node, depth = memory.pop(0)
            else:
                node = None

        return depth