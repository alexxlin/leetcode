class Solution:
    def trap(self, height: List[int]) -> int:
        
        # water is trapped from side to the middle, so we are tracking 
the maximum we see as we move toward the middle
        # amount trap is determined by the lesser of left/right
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]
        result = 0
        while left < right:
            if left_max < right_max:
                result += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                result += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        
        return result

