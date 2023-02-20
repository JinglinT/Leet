class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        maxProfit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[low]
            if profit > maxProfit:
                maxProfit = profit
            if prices[i] < prices[low]:
                low = i

        return maxProfit
