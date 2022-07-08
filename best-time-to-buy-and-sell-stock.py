"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, ans = prices[0], 0

        for i in range(len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            else:
                profit = prices[i] - buy
            ans = max(ans, profit)

        return ans


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))