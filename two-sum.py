class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_dict = {}

        for i, v in enumerate(nums):
            if v in num_dict:
                num_dict[v].append(i)
            else:
                num_dict[v] = [i]

        print(num_dict)

        for n in nums:
            m = target - n
            if m in num_dict:
                if m != n:
                    return [num_dict[n][0], num_dict[m][0]]
                elif len(num_dict[m]) > 1:
                    return num_dict[m]

"""
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
"""

solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))

