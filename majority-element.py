"""

https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr, count = nums[0], 1                   # curr will store the current majority element, count will store the count of the majority
        for i in nums[1:]:
            count += (1 if curr == i else -1)      # if i is equal to current majority, they're in same team, hence added, else one current majority and i both will be dead
            if not count:                          # if count of current majority is zero, then change the majority element, and start its count from 1
                curr = i
                count = 1
        return curr


sol = Solution()
print(sol.majorityElement([3, 2, 3]))