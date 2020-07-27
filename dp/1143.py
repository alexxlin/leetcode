class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #time: O(nk)
        #space: O(nk)
        
        #basecase
        if len(text1) == 0 or len(text2) == 0:
            return 0
        
        #using hint 1, DP[i][j] for substring text1[:i], text2[:j]
             
        #needs to add a character to text1/2, since the for loops start from 1
        text1 = ' ' + text1
        text2 = ' ' + text2
        
        dp = [[0 for j in range(len(text2))] for i in range(len(text1))]   

        for i in range(1, len(text1)):
            
            for j in range(1, len(text2)):
                                            
                if text1[i] == text2[j]:
        
                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:
                    
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                

        return dp[len(text1) - 1][len(text2) - 1]
                