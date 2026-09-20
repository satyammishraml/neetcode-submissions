class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = float("inf")
        max_profit = 0
        for price in prices:
            if price <  buying_price:
                buying_price = price
            max_profit = max(price - buying_price, max_profit)
        return max_profit


""""
1. 
buying_price = float(inf)
for price in prices:
    if price < buying_price:
        buying_price = price
2.
max_profit = 0
for selling_price in prices:
    profit = selling_price - buying_price
    max_profit = max(profit, max_profit)

3.Merge 
buying_price = float(inf)
profit = 0
for price in prices:
    if price < buying_price:
       price =  buying_price
    max_profit = max(profit, price - buying_price)
return max_profit


"""





