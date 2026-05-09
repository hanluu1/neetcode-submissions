class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left, right = 0, 1
        for right in range(len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            else:
                left = right 
            
            print(maxProfit)
        return maxProfit

