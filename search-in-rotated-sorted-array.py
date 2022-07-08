class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        print(nums, target)
        while left <= right:
            i = (left + right) // 2
            print(f"l = {left}, i = {i}, r = {right}")
            go_right = False
            if nums[i] < target:
                if target <= nums[right] or nums[i] > nums[right]:
                    go_right = True
            elif target < nums[i]:
                if target < nums[left] <= nums[i]:
                    go_right = True
            else:
                return i

            if go_right:
                left = i + 1
            else:
                right = i - 1

        return -1

sol = Solution()
print(sol.search([1], 1))  # 0
print(sol.search([3], 1))  # -1
print(sol.search([3, 1], 1))  # 1
print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
print(sol.search([4, 5, 6, 7, 8, 1, 2, 3], 8))  # 4