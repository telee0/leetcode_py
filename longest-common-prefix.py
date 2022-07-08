class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        min_i = len(strs[0])

        for s in strs[1:]:
            if min_i <= 0:
                return ""
            i = 0
            n = len(s)
            for c in strs[0]:
                if i < n and s[i] == c:
                    i += 1
                else:
                    break
                if i >= min_i:
                    break
            if i < min_i:
               min_i = i

        return strs[0][0:min_i]

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))