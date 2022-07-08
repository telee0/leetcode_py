class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n - 1

        swapped = False

        while j > 0:
            i = j - 1
            # print(i, j)
            if nums[i] < nums[j]:
                nums[j:] = list(reversed(nums[j:]))
                for k in range (j, n):
                    if nums[k] > nums[i]:
                        x = nums[i]
                        nums[i] = nums[k]
                        nums[k] = x
                        break
                swapped = True
                break
            j -=1

        if not swapped: nums.reverse()

        return nums

sol = Solution()
print(sol.nextPermutation([1, 2, 3]))
print(sol.nextPermutation([2, 3, 1]))
print(sol.nextPermutation([3, 2, 1]))
print(sol.nextPermutation([1, 1, 5]))
print(sol.nextPermutation([1, 3, 2, 5, 4, 3]))
