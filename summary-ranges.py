"""

https://leetcode.com/problems/summary-ranges/

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        ranges = []
        start, stop, prev = nums[0], nums[0], nums[0]

        for i in range(len(nums)):
            # print('n = {0}, {1}-{2}, prev = {3}'.format(nums[i], start, stop, prev))
            if nums[i] == prev + 1:
                stop = nums[i]
            elif nums[i] > prev + 1:
                r = '{}'.format(start) if start == stop else '{}->{}'.format(start, stop)
                ranges.append(r)
                start, stop = nums[i], nums[i]
            if i == len(nums) - 1:
                r = '{}'.format(start) if start == stop else '{}->{}'.format(start, stop)
                ranges.append(r)
            prev = nums[i]

        return ranges


sol = Solution()
print(sol.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
