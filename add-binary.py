"""

https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        b1 = int(a, 2)
        b2 = int(b, 2)
        return format(b1 + b2, 'b')

sol = Solution()
print(sol.addBinary("11", "1"))
print(sol.addBinary("1010", "1011"))