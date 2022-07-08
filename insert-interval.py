"""

https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)

        if n == 0:
            return [newInterval]

        indexes = [0, 0]

        for k in [0, 1]:
            left = 0
            right = n - 1
            while left <= right:
                i = (left + right) // 2
                # print(f"{k}: l = {left}, i = {i}, r = {right}")
                if intervals[i][k] < newInterval[k]:
                    left = i + 1
                elif intervals[i][k] > newInterval[k]:
                    right = i - 1
                else:
                    break
            indexes[k] = i

        print(indexes)

        if newInterval[0] > intervals[indexes[0]][1]:
            indexes[0] = indexes[0] + 1 if indexes[0] < n - 1 else n - 1
            left = newInterval[0]
        else:
            left = min(intervals[indexes[0]][0], newInterval[0])

        if newInterval[1] < intervals[indexes[1]][0]:
            right = newInterval[1]
        else:
            right = max(intervals[indexes[1]][1], newInterval[1])
            indexes[1] = indexes[1] + 1 if indexes[1] < n - 1 else n - 1

        print(indexes)

        return intervals[0:indexes[0]] + [[left, right]] + intervals[indexes[1]:]

        # return [indexes, newInterval, intervals, ">>> ", intervals2]

sol = Solution()
print(sol.insert([[1, 3], [6, 9]], [2, 5]))
# print(sol.insert([[1, 3],[6, 9]], [2, 5]))
# print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
