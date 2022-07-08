"""

https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n, m = len(s), len(t)

        if n == 0:
            return True
        elif m == 0:
            return False

        found = False

        i, j = 0, 0

        while i < n:
            found = False
            while j < m:
                print(s[0:i+1], t[0:j+1])
                if s[i] == t[j]:
                    found = True
                    j += 1
                    break
                j += 1
            if not found:
                return False
            i += 1

        return found


sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("axc", "ahbgdc"))
print(sol.isSubsequence("aaaaaa", "bbaaaa"))
