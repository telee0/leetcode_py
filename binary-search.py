"""

https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            i = (left + right) // 2
            print(f"l = {left}, i = {i}, r = {right}")
            if nums[i] < target:
                left = i + 1
            elif nums[i] > target:
                right = i - 1
            else:
                return i

        return -1


sol = Solution()
# print(sol.search([1, 3, 5, 7], 10))
# print(sol.search([1, 3, 5, 7, 9], 10))
# print(sol.search([1, 3], 4))
print(sol.search([1], 4))