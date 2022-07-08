class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        sign = 0

        if dividend < 0:
            sign -= 1
            if dividend < INT_MIN:
                dividend = INT_MIN
            dividend = 0 - dividend
        elif dividend > INT_MAX:
            dividend = INT_MAX
        if divisor < 0:
            sign -= 1
            if divisor < INT_MIN:
                divisor = INT_MIN
            divisor = 0 - divisor
        elif divisor > INT_MAX:
            divisor = INT_MAX

        if divisor == 1:
            if sign == -1:
                return max(0 - dividend, INT_MIN)
            else:
                return min(dividend, INT_MAX)

        divisors = [divisor]
        if divisor < 1000:
            d = divisor
            for i in range(4):
                d = d + d + d + d + d
                d = d + d
                divisors.append(d)

        print(divisors)

        q = 0
        r = dividend
        for d in reversed(divisors):
            print(f"r = {r}, q = {q}, d = {d}")
            while r >= d:
                r -= d
                q += 1
            if d > divisor:
                q = q + q + q + q + q
                q = q + q

        q = 0 - q if sign == -1 else q

        if q < INT_MIN:
            q = INT_MIN
        elif q > INT_MAX:
            q = INT_MAX

        return q

sol = Solution()
# print(sol.divide(-2147483648, -10))
# print(sol.divide(7, -3))
# print(sol.divide(2147483647, 3))
print(sol.divide(-1060849722, 99958928))


