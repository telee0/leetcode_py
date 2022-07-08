class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(abs(x))

        reversed = int(s[::-1])

        if reversed > 2147483647:
            return 0

        return reversed if x > 0 else (reversed * -1)

        #
        # original
        #

        s = "%s" % x

        if s[0] == '-':
            s = s[:-len(s):-1]
            sign = -1
        else:
            s = s[::-1]
            sign = 1

        val = int(s)

        # print(f"x = {x} val = {val}")

        return 0 if val >> 31 else sign * val


sol = Solution()
print(sol.reverse(1563847412))
# print(sol.reverse(2147483647))
