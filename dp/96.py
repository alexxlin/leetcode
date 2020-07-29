class Solution:
    def numTrees(self, n: int) -> int:
        
        #time: O(n ** 2)
        #space: O(n)
        
        dp = [0] * (n + 1)
        
        #if no node, still one BST (nothing) this is to be used for when a root's
        #left/right subtree has no node
        dp[0] = 1
        #if one node, one BST
        dp[1] = 1
        
        #compute unique BST for each i
        for i in range(2, n + 1):
            
            count = 0
            
            #if j is 5, its left subtree could be all unique BSTs of 1 to 4 nodes
            #its right subtree could be all unique BSTs of 6 to n nodes
            for j in range(1, i + 1):
                count += dp[j - 1] * dp[i - j]
                
            dp[i] = count
            
        return dp[n]
                