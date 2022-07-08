"""
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        memory = set()
        while True:
            digits = [int(c) for c in str(num)]
            sum = 0
            for d in digits:
                sum += d * d
            if sum == 1:
                return True
            elif sum in memory:
                return False
            else:
                memory.add(sum)
            num = sum


sol = Solution()
print(sol.isHappy(1))
print(sol.isHappy(2))
print(sol.isHappy(19))
