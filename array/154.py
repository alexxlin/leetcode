class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #revised binary search
        #comparing mid with right only (found no solution comparing with nums[0] or left)
        #also if mid == right, can't make conclusion, thus right-- conservative approach
        
        #time: average O(logn), worst case O(n)
        #space: O(1)
        
        def binary_search(left, right):

            if (right - left) <= 1:
                return min(nums[left], nums[right])
            
            mid = (left + right) // 2
                        
            #mid in first partition
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
                
            else:
                right -= 1
                
                
            return binary_search(left, right)
        
        if nums == []:
            return -1
        
        #not really rotated, just an sorted array...
        if nums[-1] > nums[0]:
            return nums[0]
        
        return binary_search(0, len(nums) - 1)