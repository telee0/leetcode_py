"""

https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.


"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return True
        max_jump = 0
        for i in range(n - 1):
            max_jump = max(max_jump-1, nums[i])
            # print(i, n-1, ": max_jump =", max_jump)
            if max_jump == 0:
                return False
            if i + max_jump >= n - 1:
                return True

        return False


sol = Solution()
print(sol.jump([2,3,1,1,4]))