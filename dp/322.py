class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #time: O(n * c)
        #space: O(n)
        
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        
        for subamount in range(1, amount + 1):
            
            minimum = math.inf
            for coin in coins:
                if subamount - coin >= 0:
                    minimum = min(minimum, dp[subamount - coin] + 1)
            dp[subamount] = minimum
        
        return -1 if dp[amount] == math.inf else dp[amount]
        