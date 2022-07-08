"""

https://leetcode.com/problems/132-pattern/

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

"""

class Solution:
    def find132pattern(self, nums) -> bool:
        n = len(nums)
        if n < 3:
            return False
        for i in range(n - 2):
            for j in range(i + 1, n - 2):

            for k in range(n - 1, i + 3, -1):
                if nums[i] < nums[k]:
                    for j in range(i + 1, k):
                        if nums[i] < nums[k] < nums[j]:
                            return True
        return False

        """
        i, j = 0, 0
        for k in range(n):
            if nums[j] < nums[k]:
                j = k
            elif nums[i] > nums[k]:
                i = k
        print("i = {0}, j = {1}, n - 1 = {2}".format(i, j, n - 1))
        return i < j < n - 1
        """

sol = Solution()
print(sol.find132pattern([1, 2, 3, 4]))
print(sol.find132pattern([3, 1, 4, 2]))
print(sol.find132pattern([-1, 3, 2, 0]))
print(sol.find132pattern([3, 5, 0, 3, 4]))
