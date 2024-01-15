class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        n = len(height)
        left, right = 0, n-1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                max_area = max(max_area, area)
                left += 1
            else:
                area = (right - left) * height[right]
                max_area = max(max_area, area)
                right -= 1
        return max_area
