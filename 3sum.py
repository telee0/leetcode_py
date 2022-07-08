class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        output = set()

        for k in range(len(s)):
            target = -s[k]
            i,j = k+1, len(s)-1
            while i < j:
                sum_two = s[i] + s[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    output.add((s[k],s[i],s[j]))
                    i += 1
                    j -= 1
        return output

        num_dict = {}

        for i in range(len(nums)):
            if nums[i] in num_dict:
                num_dict[nums[i]].append(i)
            else:
                num_dict[nums[i]] = [i]

        num_list = []
        nl_dict = {}

        for i in range(len(nums)):
            nl = self.twoSum(nums, num_dict, i)
            if len(nl) > 0:
                for l in nl:
                    key = "%s:%s:%s" % tuple(l)
                    if not key in nl_dict:
                        nl_dict[key] = 1
                        num_list.append(l)

        return num_list

    def twoSum(self, nums, num_dict, i):
        num1 = nums[i]
        num_list = []
        for num2 in num_dict:
            num3 = -num1 - num2
            if num3 in num_dict:
                for j in num_dict[num2]:
                    for k in num_dict[num3]:
                        if i < j and j < k:
                          num_list.append(sorted([nums[i], nums[j], nums[k]]))
        return num_list


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))