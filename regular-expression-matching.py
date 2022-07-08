class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        i = j = 0
        m = len(s)
        n = len(p)

        match_any = False
        match_char = '_'

        backup = []

        while i < m and j < n:
            match_once = True
            if p[j] == '.':
                match_any = True
            elif p[j] == '*':
                match_once = False
            else:
                match_char = p[j]
                match_any = False

            print(f"({i}, {j}) s = {s[i:m]}, p = {p[j:n]}, ma = {match_any}, mc = '{match_char}', mo = {match_once}")

            if not match_once:
                ii = i - 1
                while ii < m and (match_any or s[ii] == match_char):
                    backup.append([ii, j + 1]) # backup to skip it
                    ii += 1
                if ii > i:
                    i = ii
            else:
                if match_any or s[i] == match_char:
                    i += 1
                # elif j + 1 < n and p[j + 1] != '*':
                #   return False

            j += 1

        print(f"--------- --------- i = {i}, j = {j}")
        print("backup = ", backup)

        if i == m:
            p_left = 0 # test if the remaining pattern can be ignored
            while j < n:
                if p[j] == '*':
                    p_left -= 1
                else:
                    p_left += 1
                j += 1

            if p_left <= 0:
                return True

        for b in backup:
            if b[0] < m and b[1] < n and self.isMatch(s[b[0]:], p[b[1]:]):
                return True

        return False


sol = Solution()
# print(sol.isMatch("b", "aaa."))
# print(sol.isMatch("a", "ab*"))
# print(sol.isMatch("aa", "a"))
# print(sol.isMatch("aa", "a*"))
# print(sol.isMatch("ab", ".*c"))
# print(sol.isMatch("aaa", "a*a"))
# print(sol.isMatch("aaa", "ab*a*c*a"))
# print(sol.isMatch("aab", "c*a*b"))
# print(sol.isMatch("aaa", "ab*ac*a"))
print(sol.isMatch("abbbcd", "ab*bbbcd"))
