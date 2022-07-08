"""

https://leetcode.com/problems/remove-covered-intervals/

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

"""


class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n, longest = len(intervals), 0
        for _, end in intervals:
            if end <= longest:
                n -= 1
            else:
                longest = end
        return n


sol = Solution()
print(sol.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
print(sol.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))
