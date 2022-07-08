"""

https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solution = set()
        c = sorted(candidates)
        i, n, c0 = 0, len(c), c[0]
        while i < n and c[i] == c0:
            i += 1
        if target % c0 == 0 and c0 * i >= target:
            solution.add((c0,) * (target // c0))
        if i < n:
            for k in range(i + 1):
                # print("i =", i, "n =", n, ", k =", k)
                if target - c0 * k > 0:
                    candidates_1 = self.combinationSum2(c[i:], target - c0 * k)
                    for c1 in candidates_1:
                        c1 = (c0,) * k + c1
                        solution.add(c1)
        return solution


sol = Solution()
# print(sol.combinationSum2([1, 2], 4))
# print(sol.combinationSum2([2, 5, 2, 1, 2], 5))
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
# print(sol.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))
# print((1, ) * 0 + (2, 3))