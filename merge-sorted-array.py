"""

https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        aux = []

        i, j = 0, 0

        while i + j < m + n:
            if i < m and j < n:
                x = nums1[i]
                y = nums2[j]
                if x <= y:
                    aux.append(x)
                    i += 1
                else:
                    aux.append(y)
                    j += 1
            elif i < m:
                while i < m:
                    aux.append(nums1[i])
                    i += 1
            else:
                while j < n:
                    aux.append(nums2[j])
                    j += 1

        nums1[:] = [a for a in aux]


sol = Solution()
# print(sol.merge([1, 2, 3, 0, 0, 0], 3, [2,5,6], 3))
# print(sol.merge([1], 1, [], 0))
print(sol.merge([2, 0], 1, [1], 1))