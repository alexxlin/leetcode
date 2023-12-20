class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = math.inf

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit
