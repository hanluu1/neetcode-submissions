class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return the maximum profit 
        left = 0
        maxProfit = 0
        for right in range(left + 1, len(prices)):
            profit = prices[right] - prices[left]
            if profit > maxProfit:
                maxProfit = profit
            elif profit < 0:
                left = right
        return maxProfit