class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #2 pointer 
        l, r = 0,1
        maxProfit = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0: 
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r+=1
        return maxProfit
