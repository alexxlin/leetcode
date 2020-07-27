class Solution:
    def decodeString(self, s: str) -> str:
        
        #time: O(n) all indices are visited once
        #space: O(k*n) basically having two copies of result
        
        output = ""
        
        def recursive(multiplier, i):
            
            result = ""
            
            while i < len(s):
                
                if s[i] == ']':
                    
                    return (result * multiplier, i)
                
                if s[i].isnumeric():
                    
                    #get the full multiplier
                    inner_multiplier = ""
                    while s[i].isnumeric():
                        inner_multiplier += s[i]
                        i += 1
                    inner_multiplier = int(inner_multiplier)
                    (recursive_result, ending_i) = recursive(inner_multiplier, i + 1)
                    i = ending_i + 1
                    result += recursive_result
                
                else:
                    result += s[i]
                    i += 1
                    
            print("error")
            return None
        
        j = 0
        while j < len(s):
            
            if s[j].isnumeric():
                
                #get the full multiplier
                multiplier = ""
                while s[j].isnumeric():
                    multiplier += s[j]
                    j += 1
                multiplier = int(multiplier)
                [recursive_result, ending_j] = recursive(multiplier, j + 1)
                output += recursive_result
                j = ending_j + 1
            else:
                output += s[j]
                j += 1
        
        return output
            
        
