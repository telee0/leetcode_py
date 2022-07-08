class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        sign = 1
        i = 0

        if len(s) > 0:
            if s[0] == '-':
                sign = -1
                i = 1
            elif s[0] == '+':
                i = 1

        num = 0

        for j in range(i, len(s)):
            if '0' <= s[j] and s[j] <= '9':
                num = num * 10 + int(s[j])
            else:
                break

        num = sign * num

        if num > 2147483647:
            return 2147483647
        elif num < -2147483648:
            return -2147483648
        else:
            return num


sol = Solution()
print(sol.myAtoi("-91283472332"))
print(sol.myAtoi("-42"))