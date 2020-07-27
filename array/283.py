class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #time: O(n)
        #space: O(1)
        
        #index to check
        i = 0
        
        #index to stop checking, as the rest are zero indices
        #that don't need checking
        end = len(nums)
        
        while i < end:
            
            if nums[i] == 0:
                nums.append(nums.pop(i))
                end -= 1
            
            else:
                i += 1