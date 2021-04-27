class Solution:
    def maxProfit(prices: List[int]) -> int:

        max_price = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)

        return max_price
