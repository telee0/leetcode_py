class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return n

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

        return right + 1


sol = Solution()
# print(sol.searchInsert([1, 3, 5, 7], 10))
# print(sol.searchInsert([1, 3, 5, 7, 9], 10))
# print(sol.searchInsert([1, 3], 4))
print(sol.searchInsert([1], 4))
