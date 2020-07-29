class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #time: O(n * k)
        #space: O (n)
        
        dp = [0] * (amount + 1)
        
        #to acheive 0 amount, we have one combination: adding no coin
        dp[0] = 1
        
        
        #different order of for loop yields different result
        
        # for subamount in range(1, amount + 1):
        #     for coin in coins:
        #         if subamount >= coin:
        for coin in coins:
            for subamount in range(coin, amount + 1):
                    dp[subamount] += dp[subamount - coin]

        return dp[amount]
    
