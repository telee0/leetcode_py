"""

https://leetcode.com/problems/count-sorted-vowel-strings/

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

"""


class Solution:
    def countVowelStrings(self, n: int) -> int:

        def count(m, v):
            if len(v) == 0:
                return 0
            c = 0
            for i in range(1, m + 1):
                c += i * count(n - i, v[1:])
            return c

        vowels = ['a', 'e', 'i', 'o', 'u']

        return count(n, vowels)


sol = Solution()
print(sol.countVowelStrings(1))
print(sol.countVowelStrings(2))
print(sol.countVowelStrings(33))
