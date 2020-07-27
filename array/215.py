class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #time: O(k * n)
        #space: O(1)
        
        for i in range(k - 1):
            
            max = -1
            for num in nums:
                if num > max:
                    max = num
            
            nums.remove(max)
        
        max = -1
        for num in nums:
            if num > max:
                max = num
                    
        return max
            
        