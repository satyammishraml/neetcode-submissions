class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = float("inf")
        max_profit = 0
        for idx, price in enumerate(prices):
            if price <  buying_price:
                buying_price = price
            max_profit = max(price - buying_price, max_profit)
        return max_profit
