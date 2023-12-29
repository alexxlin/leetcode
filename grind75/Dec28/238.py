class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        left[0] = nums[0]
        right[-1] = nums[-1]
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i]
        
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i]
        
        result = [1] * n
        result[0] = right[1]
        result[-1] = left[-2]
        for i in range(1, n-1):
            result[i] = left[i-1] * right[i+1]
        
        return result

