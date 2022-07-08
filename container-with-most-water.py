class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        max_area = 0

        i = 0
        j = n - 1

        while i < j:
            area = min(height[i], height[j]) * (j - i)

            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            elif height[i + 1] > height[i]:
                i += 1
            else:
                j -= 1

            if area > max_area:
                max_area = area

        return max_area


"""
        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                if area > max_area:
                    max_area = area

        return max_area
"""

sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea([1, 1]))
