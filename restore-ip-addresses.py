"""

https://leetcode.com/problems/restore-ip-addresses/

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

"""


class Solution(object):
    def stringToOctets(self, s, n):


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        octets = []

        if s[0] == '0':
            octet =  '.'.join(['0'] + restoreIpAddresses(s[1:]))



sol = Solution()
print(sol.restoreIpAddresses("25525511135"))