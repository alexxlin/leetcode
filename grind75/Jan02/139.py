class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # knapsack problem
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)+1):
            for word in wordDict:
                n = len(word)
                if i - n >= 0 and dp[i-n] and s[i-n:i] == word:
                    dp[i] = True
        
        return dp[-1]
