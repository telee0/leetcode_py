class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        out = [0, len(nums) - 1]
        c = 0
        for n in [target - 1, target + 1]:
            left, right = 0, len(nums) - 1
            i = -1
            while left <= right:
                i = (left + right) // 2
                print(f"l = {left}, i = {i}, r = {right}")
                if nums[i] < n:
                    left = i + 1
                elif n < nums[i]:
                    right = i - 1
                else:
                    break
            out[c] = i
            c += 1
        print(out)
        while 0 <= out[0] <= len(nums) - 1:
            if nums[out[0]] < target:
                out[0] += 1
            elif nums[out[0]] > target:
                out[0] = -1
                break
            else:
                break
        if out[0] == len(nums):
            return [-1, -1]
        while 0 <= out[1] <= len(nums) - 1:
            if target < nums[out[1]]:
                out[1] -= 1
            elif nums[out[1]] < target:
                out[1] = -1
                break
            else:
                break

        return out


sol = Solution()
print(sol.searchRange([2, 2], 1))
print(sol.searchRange([2, 2], 3))
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))
print(sol.searchRange([], 0))
