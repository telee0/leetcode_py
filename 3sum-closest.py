class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = sorted(nums)

        min_diff = 999

        for k in range(len(s)):
            t = target - s[k]
            i, j = k + 1, len(s) - 1
            while i < j:
                sum_two = s[i] + s[j]

                diff = abs(t - sum_two)
                if min_diff > diff:
                    min_diff = diff
                    result = s[k] + s[i] + s[j]

                if sum_two < t:
                    i += 1
                elif sum_two > t:
                    j -= 1
                else:
                    return s[k] + s[i] + s[j]
                    i += 1
                    j -= 1

        return result


sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))