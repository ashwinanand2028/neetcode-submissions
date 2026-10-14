class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curMin = prices[0]

        profit = 0

        for price in prices:

            curMin = min(curMin, price)
            profit = max(profit, price - curMin)
        
        return profit