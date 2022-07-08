"""

https://leetcode.com/problems/remove-k-digits/

Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

https://iq.opengenus.org/remove-k-digits-to-make-smallest-number/

"""
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for d in num:
            while k > 0 and len(stack) > 0 and stack[-1] > d:
                k -= 1
                stack.pop()
            stack.append(d)

        if k > 0:
            stack = stack[:-k]

        s = "".join(stack)
        s = s.lstrip("0")

        return s if len(s) > 0 else "0"


sol = Solution()
print(sol.removeKdigits("9", 1))
print(sol.removeKdigits("10", 2))
print(sol.removeKdigits("10200", 1))
print(sol.removeKdigits("1432219", 3))