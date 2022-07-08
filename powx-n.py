"""

https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        z, y, i = 1, x, 1
        while m > 0:
            if i * 2 <= m:
                y *= y
                i *= 2
            else:
                z *= y
                m -= i
                y, i = x, 1

        if n < 0:
            z = 1 / z
        return z

sol = Solution()
print(sol.myPow(2.00000, 10))