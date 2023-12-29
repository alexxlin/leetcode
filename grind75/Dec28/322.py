class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #knapsack, inifinite amount of each item
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        if dp[-1] == math.inf:
            return -1
        return dp[-1]
