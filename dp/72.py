class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        #time: O(n*m)
        #space: O(n*m)

        #basecase
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        
        dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        
        #if one of the string is empty, return length of the other string:
        for j in range(len(word2) + 1):
            dp[0][j] = j
            
        for i in range(len(word1) + 1):
            dp[i][0] = i
            
        
        #shifting all i, j forward by 1
        for i in range(1, len(word1) + 1):      
            for j in range(1, len(word2) + 1):
                
                #two characters are equal, no need to add operation
                #since all i and j are shifted by one, here we use i - 1/j - 1 for word[]
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    
                else:
                    #replace for dp[i-1][j-1]
                    #insert/delete for dp[i-1][j], dp[i][j-1]
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    
        
        return dp[len(word1)][len(word2)]
        
        