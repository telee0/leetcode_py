"""

https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        t = s[::-1]

        return s == t

        # return (lambda an: an == an[::-1])("".join(filter(str.isalnum, s)).lower())

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))