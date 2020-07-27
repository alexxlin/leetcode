class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        #method 1: recursion
        
#         def recursive_LIS(nums, previous):
            
#             if len(nums) == 0:
#                 return 0
            
#             included = 0
            
#             if nums[0] > previous:
                
#                 included = 1 + recursive_LIS(nums[1:], nums[0])
                
#             not_included = recursive_LIS(nums[1:], previous)
                
#             return max(included, not_included)
        
#         return recursive_LIS(nums, - math.inf)
    
        #method 2: recursion with memo
        
        #time: O(n ** 2) filling out all memo with previous < start, O((n+1) * (n) / 2)
        # = O(n ** 2)
        #space: O(n ** 2) memo size
        
#         nums = [- math.inf] + nums
#         memo = [[None for j in range(len(nums))] for i in range(len(nums))]
        
#         def recursive_LIS(nums, previous, starting, memo):
            
#             if len(nums) == 0 or starting == len(nums):
#                 return 0
            
#             if memo[previous][starting]:
#                 return memo[previous][starting]
            
#             included = 0
            
#             if nums[starting] > nums[previous]:
                
#                 included = 1 + recursive_LIS(nums, starting, starting + 1, memo)
                    
#             not_included = recursive_LIS(nums, previous, starting + 1, memo)

#             result = max(included, not_included)
#             memo[previous][starting] = result
#             return result
        
#         return recursive_LIS(nums, 0, 1, memo)

        #method 3: DP
    
        #time: O(n ** 2)
        #space: O(n)
    
        #basecase
        if len(nums) == 0:
            return 0
        
        dp = [None] * len(nums)
        
        
        for i in range(len(nums)):
            
            #keeps track of the LIS in nums[:i]
            LIS = 0
            
            for j in range(i):
                
                #j could be included in i's LIS
                if nums[j] < nums[i]:
                    
                    LIS = max(LIS, dp[j])
                
            dp[i] = LIS + 1
            
        return dp[-1]
    
        #method 4: dp with binary search
    
    
    
                
                    
        
        
                    
                
            
            