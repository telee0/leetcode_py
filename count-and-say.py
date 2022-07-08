"""

https://leetcode.com/problems/count-and-say/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s, x, count = "1", '1', 0
        while n > 1:
            t = ""
            for c in s:
                if c != x:
                    if count > 0:
                        t += str(count) + x
                    x, count = c, 1
                else:
                    count += 1
            if count > 0:
                t += str(count) + x
            s, x, count = t, t[0], 0
            # print(n, ": s =", s, ", x =", x, ", count =", count, ", temp =", temp)
            n -= 1

        return s


sol = Solution()
print(sol.countAndSay(1))
print(sol.countAndSay(2))
print(sol.countAndSay(3))
print(sol.countAndSay(4))
