"""

https://leetcode.com/problems/reducing-dishes/

A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

"""

class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        n = len(satisfaction)

        s = sorted(satisfaction)
        print(s)
        sum = 0

        for i in range(n):
            sum += s[i] * (i + 1)

        return sum

sol = Solution()
print(sol.maxSatisfaction([-1, -8, 0, 5, -9]))
print(sol.maxSatisfaction([4, 3, 2]))