class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #binary search
        #time: O(logn)
        #space: O(1)
        
        def searchFirst(left, right, target):
            
            if left == right:
                if nums[left] == target:
                    return left
                return -1
            
            
            if left == right - 1:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                return -1
            
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
            
            return searchFirst(left, right, target)
        
        
        def searchLast(left, right, target):
            

            if left == right:

                if nums[left] == target:

                    return left
                return -1
            
            if left == right - 1:

                if nums[right] == target:

                    return right
                elif nums[left] == target:

                    return left
                return -1
            
            mid = (left + right) // 2
            
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
            
            return searchLast(left, right, target)
        
        if len(nums) == 0:
            return [-1, -1]
        
        first = searchFirst(0, len(nums) - 1, target)
        last = searchLast(0, len(nums) - 1, target)
        
        return [first, last]