"""

https://leetcode.com/problems/delete-and-earn/

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

"""

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return nums[0]

        memory = nums.toset

        for i in range(n):
            pass

        return memory


sol = Solution()
print(sol.deleteAndEarn([3,4,2]))