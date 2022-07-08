"""

https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = 1
        right = x // 2

        while left <= right:
            i = (left + right) // 2
            print(f"l = {left}, i = {i}, r = {right}")
            if i * i < x:
                left = i + 1
            elif i * i > x:
                right = i - 1
            else:
                return i

        return left - 1 if left * left > x else left

sol = Solution()
print(sol.mySqrt(99))
print(sol.mySqrt(255))
print(sol.mySqrt(256))