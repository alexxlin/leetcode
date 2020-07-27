class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        #check the four corners, top-right and bot-right are interesting
        #moving one direction will decrease, while the other will increase
        
        #time: O(m + n)
        #space: O(1)
        
        #basecase
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        #start at top right        
        row = 0
        column = -1
        
        previous_checking = [-1, -1]
        
        while row < len(matrix) and column >= -len(matrix[0]):
            
            checking = matrix[row][column]
            
            if target == checking:
                return True
            
            if [row, column] == previous_checking:
                print(1)
                return False
            
            previous_checking = [row, column]
            
            if target < checking:
                column -= 1
            else:
                row += 1
        
        return False