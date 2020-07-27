class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #revised binary search
        #the array can be seen as two partitions: before and after pivot
        #if target greater than num[0], its in first partition
        #else in second partition
        
        #time: O(logn)
        #space: O(1)
            
        #helper recursive
        def revised_binary(left, right, target):
            
            if left == right:
                if nums[left] == target:
                    return left
                return -1
            
            if left == right -1:
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                return -1
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            #target is in first partition
            if first_part:
                  
                #mid is in first partition, and less than target -> to the left of target
                if nums[0] <= nums[mid] < target:
                    left = mid
                else:
                    right = mid
                  
            #target is in second partition
            else:
                
                #mid is in second partition and greater than target -> mid is at right of target
                if target < nums[mid] < nums[0]:
                    right = mid
                else:
                    left = mid
            
            return revised_binary(left, right, target)
        
        if nums == []:
            return -1
        
        if target >= nums[0]:
            first_part = True
        else:
            first_part = False
            
        return revised_binary(0, len(nums) - 1, target)