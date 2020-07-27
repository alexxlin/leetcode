class Solution:
    def trap(self, height: List[int]) -> int:
        
        # if there are two numbers (i, j) greater than x
        #than the area between them can trap x * (j - i) water,
        #minus height
        #two pointers apporach, left and right
        
        #time: O(n)
        #space: O(1)
        
        #basecase
        if len(height) < 3:
            return 0
        
        left = 0
        right = len(height) - 1
        
        current_height = 0
        moving_right = True
        
        result = 0
        
        while left != right:

                
            if (moving_right and height[left] > current_height)\
            or (not moving_right and height[right] > current_height):
                
                current_height = min(height[left], height[right])

                #if left is taller than right, move right pointer toward left
                if height[left] >= height[right]:
                    moving_right = False
                else:
                    moving_right = True
            
            if moving_right:
                result += max(0, current_height - height[left])
                left += 1
            else:
                result += max(0, current_height - height[right])
                right -= 1
            
        return result
                    
        

