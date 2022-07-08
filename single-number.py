class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for num in nums:
            xor ^= num

        return xor


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))