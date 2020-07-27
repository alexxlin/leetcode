class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #two partitions, min will be at the beginning of second partition
        #use binary search
        
        #time: O(logn)
        #space: O(1)
        
        def binary_search(left, right):
            
            if (right - left) <= 1:
                return min(nums[left], nums[right])
            
            mid = (left + right) // 2
            
            #mid in first partition
            if nums[mid] >= nums[0]:
                left = mid
            else:
                right = mid
                
            return binary_search(left, right)
        
        if nums == []:
            return -1
        
        #not really rotated, just an sorted array...
        if nums[-1] > nums[0]:
            return nums[0]
        
        return binary_search(0, len(nums) - 1)