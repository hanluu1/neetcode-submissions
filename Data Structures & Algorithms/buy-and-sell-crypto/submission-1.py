class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #the price of the day before has to be less than the price of the day after
        #iterate find the different of price between days and return the max profit
        maxProfit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                maxProfit = max(maxProfit, profit)
        return maxProfit