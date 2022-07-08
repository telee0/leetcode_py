"""

https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

"""

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0, 1]

        if n == 0:
            return ans[0:1]

        for i in range(2, n + 1):
            if (i - 1) % 2 == 0:
                bits_1 = ans[i - 1] + 1
            else:
                bits_1 = ans[i // 2]
            ans.append(bits_1)

        return ans


sol = Solution()
print(sol.countBits(10))