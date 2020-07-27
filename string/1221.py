class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        counter = 0
        
        result = 0
        
        for c in s:
            
            if c == 'R':
                counter += 1
            else:
                counter -= 1
                
            if counter == 0:
                result += 1
        
        return result