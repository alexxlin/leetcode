class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        #binary search, first search the rows to check
        #on specified row, binary search for the column
        
        #time: O(logm + logn)
        #space: O(m + n) if I use while loop instead of recursion, it would be O(1)
        
        #basecase
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        top = 0
        bot = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        #passing in the right-most column of matrix
        def binary_search_row(column, top, bot, target):
            
            if top == bot:
                return top
            
            if top == bot - 1:
                if target <= column[top]:
                    return top
                else:
                    return bot
            
            #heard that this is safer than mid = (top + bot) // 2
            mid = top + (bot - top) // 2
            
            if target <= column[mid]:
                bot = mid
            else:
                top = mid
            
            return binary_search_row(column, top, bot, target)
        
        def binary_search_column(row, left, right, target):
            
            #base cases
            if (right - left) <= 1:
                return row[left] == target or row[right] == target
            
            mid = left + (right - left) // 2
            
            if target <= row[mid]:
                right = mid
            else:
                left = mid
            
            return binary_search_column(row, left, right, target) 
        
        #constructing left most column of given matrix
        left_most_column = [x[-1] for x in matrix]
        
        row = binary_search_row(left_most_column, top, bot, target)
        
        return binary_search_column(matrix[row], left, right, target)
        
        