class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #two pointers method.
        #the area is determined by the shortest side. each time
        #moving the pointer of the shorter side toward the middle.
        
        left = 0
        right = len(height) - 1
        maximum = -1
        
        while left != right:
            
            area = (right - left) * min(height[left], height[right])
            
            if area > maximum:
                maximum = area
                
            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
                
        return maximum