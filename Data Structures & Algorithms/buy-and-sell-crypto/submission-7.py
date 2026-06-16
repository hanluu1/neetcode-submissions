class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window
        l,r = 0, 1
        ans = 0
        #if left less than right then profit = right -left
        #if not then left move to right
        #right move up then compare again if right larger then find profit again
        #store profit to ans
        #move right again until having the max profit value. 
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l+=1                
            elif profit > 0:
                ans = max(ans,profit)
            r+=1
        return ans



