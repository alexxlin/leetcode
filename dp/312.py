class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        #1. recursion with memo
        #memo[left][right] stores the maximum coin gain for a given boundary left and right
        
        #time: O(n ** 3)? there is a for loop, and all memo would be visited once in the for loop?
        #space: O(n ** 2)
        
#         def optimal_burst(left, right, memo, nums):

#             if left == right - 1:
#                 return 0

#             if memo[left][right] != -1:
#                 return memo[left][right]

#             result = 0

#             #brute force
#             #this would give you the series of optimal ballon bursts
#             #within left and right
#             #note that in each iteration, i would be the last ballon 
#             #to burst thus it sets the boundary between left and right
#             for i in range(left + 1, right):
    
#                 #in recursion, i would be pop last, thus i's left and right
#                 #would be the actual left and right, all other ballons would be popped
#                 result = max(result, nums[left] * nums[i] * nums[right] \
#                         + optimal_burst(left, i, memo, nums) \
#                         + optimal_burst(i, right, memo, nums)) 

#             memo[left][right] = result

#             return result
    
#         #1， recursion with memo
#         #it stores the maximum coin in the [left][right] interval
#         nums = [1] + nums + [1]
#         memo = [[-1 for j in range(len(nums))] for i in range(len(nums))]
        
#         return optimal_burst(0, len(nums) - 1, memo, nums)
    
        #2. DP bottom up
        #like memo, dp stores the maximum coin gain for a given left/right
        
        #time: O(n ** 3)
        #space: O(n ** 2)
        
        nums = [1] + nums + [1]
        
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
        
        #setting basecases
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                  
                #only one ballon to pop between boundaries
                if right == left + 2:
                    dp[left][right] = nums[left] * nums[left + 1] * nums[right]
                    
        #computing dp
        for k in range(3, len(nums)):
            for left in range(0, len(nums)):
                
                #this way we will compute all cases where right = left + 1, then right = left + 2...
                right = left + k
                
                if right >= len(nums):
                    continue
                
                optimal = -1
                
                for i in range(left + 1, right):
                    
                    optimal = max(optimal, nums[left] * nums[i] * nums[right] + \
                                 dp[left][i] + dp[i][right])
                
                dp[left][right] = optimal
                
        return dp[0][len(nums) - 1]
                
                    
        
                
        
        
    
        
       