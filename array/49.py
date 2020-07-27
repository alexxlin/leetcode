class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #time: O(n k log k)
        #space: O(nk)
        
        #split all strs into letters, have a dict that maps letters to index in list
        letters_to_index = {}
        result = []
        i = 0
        
        for s in strs:
            
            #converting "eat", "tea", "ate" all to "aet"
            letters = ''.join(sorted(s))
            #if the letters are already in mapping, assign the result index to that str
            if letters in letters_to_index:
                # str_to_index[s] = letters_to_index[letters]
                result[letters_to_index[letters]].append(s)
            
            
            else:
                letters_to_index[letters] = i
                i += 1
                result.append([s])
            
        return result