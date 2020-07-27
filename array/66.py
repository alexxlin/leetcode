class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        last_digit = digits[-class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        last_digit = digits[-1]
        
        if last_digit == 9:
            i = -1
            
            #loop through digits, change 9s to 0s
            while digits[i] == 9 and i != -len(digits):                
                digits[i] = 0
                i -= 1
            
            #after the loop, if at left most digit, convert 99 to 100  
            if i == -len(digits) and digits[i] == 9:                
                
                digits[i] = 0
                digits.insert(0, 1)
                
            #otherwise just increment left most digit by 1   
            else:
                digits[i] += 1
        else:
            digits[-1] = digits[-1] + 1
        return digits1]
        
        if last_digit == 9:
            i = -1
            
            #loop through digits, change 9s to 0s
            while digits[i] == 9 and i != -len(digits):                
                digits[i] = 0
                i -= 1
            
            #after the loop, if at left most digit, convert 99 to 100  
            if i == -len(digits) and digits[i] == 9:                
                
                digits[i] = 0
                digits.insert(0, 1)
                
            #otherwise just increment left most digit by 1   
            else:
                digits[i] += 1
        else:
            digits[-1] = digits[-1] + 1
        return digits