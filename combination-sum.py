"""

https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

"""


class Solution(object):
    count = 0

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = set()

        for n in candidates:
            # print(target, "<>", n)
            if target == n:
                output.add((n,))
            elif target > n:
                candidates_1 = self.combinationSum(candidates, target - n)
                for c in candidates_1:
                    c = tuple(sorted((n,) + c))
                    output.add(c)
            if len(output) >= 150:
                break
            # print("target =", target, output)
            #if len(candidates) > 1:
            #    output.union(self.combinationSum(candidates[1:], target))

        return output

sol = Solution()
# print(sol.combinationSum([1, 2], 4))
# print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([2, 7, 6, 3, 5, 1], 9))
