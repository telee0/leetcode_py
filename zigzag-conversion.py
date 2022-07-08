class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        out = []

        for i in range(numRows):
            out.append([])

        i = 0
        move_down = True

        for c in s:
            # print(f"i = {i}, c = {c}")
            out[i].append(c)
            if move_down:
                if i + 1 < numRows:
                    i += 1
                else:
                    move_down = False
                    i -= 1
            else:
                if i > 0:
                    i -= 1
                else:
                    move_down = True
                    i += 1

        out_list = []

        for i in range(numRows):
            out_list += out[i]

        out_string = "".join(out_list)

        return out_string

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("PAYPALISHIRING", 4))
print(sol.convert("PAYPALISHIRING", 1))
print(sol.convert("A", 1))