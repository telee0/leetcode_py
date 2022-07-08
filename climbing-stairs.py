"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [0] * (n + 1)
        ways[0] = 1
        ways[1] = 1
        for i in range(2, n + 1, 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]

        #
        #
        #

        if n == 1:
            return 1

        ways = [1, 2]
        more_ways = True
        while more_ways:
            more_ways = False
            # print(ways)
            for i in range(len(ways)):
                w = ways[i]
                if w + 1 <= n:
                    ways[i] += 1
                    more_ways = True
                if w + 2 <= n:
                    ways.append(w + 2)
                    more_ways = True
            if not more_ways:
                break
        return len(ways)


sol = Solution()
# print("2", sol.climbStairs(2))
# print("3", sol.climbStairs(3))
# print("5", sol.climbStairs(5))
# print("10", sol.climbStairs(10))
print("35", sol.climbStairs(35))
