class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ints = [1000, 500, 100, 50, 10, 5, 1]
        # syms = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        syms_dict = {'M': 0, 'D': 1, 'C': 2, 'L': 3, 'X': 4, 'V': 5, 'I': 6}

        integer = 0
        j = 0

        for c in s:
            i = syms_dict[c]
            integer += ints[i]
            if j > i:
                integer += - 2 * ints[j]
            print(f"c = {c}, ({i}, {j}) {ints[i]}, integer = {integer}")
            j = i

        return integer


sol = Solution()
print(sol.romanToInt("MCMXCIV"))
