"""

https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
            elif length > 0:
                break
        return length

        #
        #
        #

        length, max_len = 0, 0
        for c in s:
            if c == ' ':
                length = 0
            else:
                length += 1
            max_len = max(max_len, length)
        return max_len


sol = Solution()
print(sol.lengthOfLastWord("hello world"))
print(sol.lengthOfLastWord("Today is a nice day"))