class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #tracking min buy and max Profit 
        maxProfit = 0
        minBuy = prices[0]
        for i in range(len(prices)):
            profit = prices[i] - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, prices[i])
        return maxProfit
