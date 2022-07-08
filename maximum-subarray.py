"""

https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum, ans = 0, float('-inf')

        for i in range(len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            ans = max(ans, sum)

        return ans

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
