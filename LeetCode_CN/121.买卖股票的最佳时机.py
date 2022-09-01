#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         result = 0
#         left = 0
#         right = 0
#         for left in range(len(prices)):
#             for right in range(left, len(prices)):
#                 result = max(result, prices[right] - prices[left])
#         return result
        
# @lc code=end

