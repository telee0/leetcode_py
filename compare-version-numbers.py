"""

https://leetcode.com/problems/compare-version-numbers/

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.


"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')

        i, n = 0, min(len(v1), len(v2))

        while i < n:
            r1 = int(v1[i])
            r2 = int(v2[i])
            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
            i += 1

        v, k = (v1, 1) if i < len(v1) else (v2, -1)

        for j in range(i, len(v)):
            r = int(v[j])
            print("r =", r)
            if r > 0:
                return k

        return 0


sol = Solution()
print(sol.compareVersion("1.0.1", "1"))
# print(sol.compareVersion("1.01", "1.001"))
