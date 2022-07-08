"""

https://leetcode.com/problems/arithmetic-slices/

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

"""

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()

        for i in range(n):
            if i + 1 < n:




sol = Solution()
print(sol.numberOfArithmeticSlices([1,2,3,4]))