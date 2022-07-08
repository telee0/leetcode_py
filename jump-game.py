"""

https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
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
# print(sol.canJump([2, 3, 1, 1, 4]))
# print(sol.canJump([3, 2, 1, 0, 4]))
print(sol.canJump([0, 2, 3]))
# print(sol.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,
#                    6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,
#                    2,2,7,5,1,7,9,6]))