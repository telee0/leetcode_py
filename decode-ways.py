"""

https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n == 0 or s[0] == '0':
            return 0

        result = 0

        if n > 1:
            r1 = self.numDecodings(s[1:])
            print("r1: {0} {1} (r1 == {2})".format(s[0], s[1:], r1))
            result += r1
        elif n == 1:
            print("r1: {0} {1} ({2})".format(s[0:1], "_", 1))
            result += 1

        if n > 2 and int(s[0:2]) < 27:
            r2 = self.numDecodings(s[2:])
            print("r2: {0} {1} (r2 == {2})".format(s[0:2], s[2:], r2))
            result += r2
        elif n == 2 and int(s[0:2]) < 27:
            print("r2: {0} {1} ({2})".format(s[0:2], "_", 1))
            result += 1

        return result


sol = Solution()
print(sol.numDecodings("12"))
print("--------- ")
print(sol.numDecodings("226"))
print("--------- ")
print(sol.numDecodings("06"))
