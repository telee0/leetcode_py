class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        start = 0
        end = m

        mid_merged = (m + n + 1) // 2

        while start <= end:
            mid = (start + end) // 2
            left1_size = mid
            left2_size = mid_merged - mid

            # checking indices
            left1_max = nums1[left1_size - 1] if (left1_size > 0) else float('-inf')
            left2_max = nums2[left2_size - 1] if (left2_size > 0) else float('-inf')
            right1_min = nums1[left1_size] if (left1_size < m) else float('inf')
            right2_min = nums2[left2_size] if (left2_size < n) else float('inf')

            if left1_max <= right2_min and left2_max <= right1_min:
                if (m + n) % 2 == 0:
                    return (max(left1_max, left2_max) + min(right1_min, right2_min)) / 2.0
                return max(left1_max, left2_max)
            elif left1_max > right2_min:
                end = mid - 1
            else:
                start = mid + 1


sol = Solution()
print(sol.findMedianSortedArrays([1, 2], [3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
