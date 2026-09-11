class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit >= 0:
                ans = max(ans, profit)
            else: l = r
        return ans
            
            