class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        s = "%s" % x

        if s == s[::-1]:
            return True

        return False