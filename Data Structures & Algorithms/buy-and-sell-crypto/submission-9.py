class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use 2 pointer
        #if the profit less than zero move left
        ans = 0
        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l += 1
            ans = max(ans, profit)
        return ans