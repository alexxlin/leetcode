class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r', 's'],
                '8':['t','u','v'],
                '9':['w','x','y', 'z'],
               }
        
        result = []
        
        def expand(previous, digits):
            
            print(previous)
            #if no more digits left
            if len(digits) == 0:
                result.append(previous)
            
            else:
                
                for letter in dict[digits[0]]:
                    expand(previous+letter, digits[1:])
        
        if digits:
            expand("", digits)
        
        return result
    

            
        
        