class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return the maximum profit can achieve
        #sum of max profits
        #sliding window having the max profit in that window 
        #if it is increasing then find the max val to get the max value
        
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit
            

