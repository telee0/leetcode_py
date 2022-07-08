class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        max_length = 0

        charset = set()

        for i, c in enumerate(s):
            right = i
            if c in charset:
                for j in range(left, right):
                    if c == s[j]:
                        left = j + 1
                        break
                    else:
                        charset.remove(s[j])
            else:
                charset.add(c)

            length = right - left + 1

            if length > max_length:
                max_length = length

        return max_length


sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
