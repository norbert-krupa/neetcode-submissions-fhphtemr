class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = max(prices)
        profit = 0

        for sell in range(len(prices)):
            if prices[sell] < buy:
                buy = prices[sell]
            else:
                profit = max(profit, prices[sell] - buy)
        
        return profit