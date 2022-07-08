class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        n = len(haystack)
        m = len(needle)

        i, j = 0, 0
        index = -1

        backup = []

        print(f"({m}, {n})")

        while i < n and j < m:
            print(f"({i}, {j}), index = {index}")
            if haystack[i] == needle[j]:
                if index < 0:
                    index = i
                j += 1
            else:
                if len(backup):
                    i = backup.pop(0) - 1
                index = -1
                j = 0
            i += 1
            k = i + m - 1
            if j > 0 and k < n:
                if haystack[i] == needle[0] and haystack[k] == needle[-1]:
                    backup.append(i)  # use backup to jump to the next candidate
                    print(f"{haystack[i:k+1]} vs {needle}")
                    print("backup =", backup)

        if j < m:
            return -1

        return index


sol = Solution()
# print(sol.strStr("hello", "ll"))
# print(sol.strStr("mississippi", "issip"))
# print(sol.strStr("mississippi", "pi"))
print(sol.strStr("mississippi", "sippi"))
# print(sol.strStr("aabaaabaaac", "aabaaac"))
