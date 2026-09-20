class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two-pointer approach: buying_pointer tracks the best day to buy seen so far,
        # selling_pointer scans forward looking for a day to sell.
        buying_pointer = 0      # index of the cheapest price found so far
        selling_pointer = 1     # index of the candidate sell day (must be after buy day)
        max_profit = 0          # best profit seen; stays 0 if prices only fall

        while selling_pointer < len(prices):
            # Profitable window: selling later than we bought, at a higher price
            if prices[selling_pointer] > prices[buying_pointer]:
                # Keep the larger of the old best and this window's profit
                max_profit = max(max_profit, prices[selling_pointer] - prices[buying_pointer])
            else:
                # Found a price <= our buy price. Any future sell is worth more
                # relative to this cheaper day, so move the buy pointer here.
                buying_pointer = selling_pointer

            selling_pointer += 1  # always advance the scan pointer

        return max_profit


"""
# Method 1 — single pass, same idea without explicit indices

        buying_price = float("inf")   # cheapest price seen so far
        max_profit = 0
        for price in prices:
            if price < buying_price:
                buying_price = price       # new cheapest buy day
            max_profit = max(price - buying_price, max_profit)
            # note: when price just became buying_price, profit is 0, so this is safe
        return max_profit


# How Method 1 is derived, in three steps:

# 1. Track the minimum price seen so far.
buying_price = float("inf")
for price in prices:
    if price < buying_price:
        buying_price = price

# 2. Given a buy price, track the best profit across all sell prices.
max_profit = 0
for selling_price in prices:
    profit = selling_price - buying_price
    max_profit = max(profit, max_profit)

# 3. Merge both loops into one pass.
buying_price = float("inf")
max_profit = 0
for price in prices:
    if price < buying_price:
        buying_price = price          # fixed: was 'price = buying_price'
    max_profit = max(max_profit, price - buying_price)
return max_profit
"""