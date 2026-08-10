class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = float("inf") 
        max_profit = 0
        for R in range(len(prices)):
            if prices[R] < bp:
                bp = prices[R]

            profit = prices[R] - bp
            max_profit = max(max_profit, profit)
        return max_profit
