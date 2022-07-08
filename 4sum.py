class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        output = set()

        for k in range(len(s)):
            for o in self.threeSum(s[k + 1:], target - s[k]):
                output.add((s[k],) + o)

        return output

    def threeSum(self, s, sum_three):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = set()

        for k in range(len(s)):
            target = sum_three - s[k]
            i, j = k + 1, len(s)-1
            while i < j:
                sum_two = s[i] + s[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    output.add((s[k], s[i], s[j]))
                    i += 1
                    j -= 1
        return output

sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0))