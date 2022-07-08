class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_length = len(s)

        max_length = 0
        max_left = 0
        max_right = 1

        for i in range(s_length):

            left = right = i

            while 0 <= left and right < s_length:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break

            left += 1
            right -= 1
            length = right - left + 1

            if length > max_length:
                max_length = length
                max_left = left
                max_right = right

            # try even pattern

            if i < s_length - 1 and s[i] == s[i + 1]:
                left = i
                right = i + 1

                while 0 <= left and right < s_length:
                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else:
                        break

                left += 1
                right -= 1
                length = right - left + 1

                if length > max_length:
                    max_length = length
                    max_left = left
                    max_right = right

        return s[max_left:max_right + 1]

sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))