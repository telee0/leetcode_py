class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ints = [1000, 500, 100, 50, 10, 5, 1]
        syms = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

        q = num // ints[0]
        num = num % ints[0]

        if q > 0:
            roman_numeral = q * syms[0]
        else:
            roman_numeral = ""

        for i in range(2, len(ints), 2):
            q = num // ints[i]
            r = num % ints[i]

            if q < 4:
                roman = q * syms[i]
            elif q < 5:
                roman = syms[i] + syms[i - 1]
            elif q < 9:
                roman = syms[i - 1] + (q - 5) * syms[i]
            else:
                roman = syms[i] + syms[i - 2]

            roman_numeral += roman

            num = r

        return roman_numeral


sol = Solution()
print(sol.intToRoman(1994))
