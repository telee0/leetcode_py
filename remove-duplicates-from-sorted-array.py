class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = nums[0]
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != last:
                nums[k] = nums[i]
                k += 1
                last = nums[i]

        return k

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))