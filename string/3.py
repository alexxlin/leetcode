class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #sliding window, shifting window to the right, then whenever encounter a repeating character, we starting from the substring just after that repeating character on the left, this ensures that the window only contains non-repeating characters
        
        #starting point
        longest = 0
        vocab = dict()
        starting = 0
        
        for index, value in enumerate(s):
            
            
            if value in vocab and vocab[value] >= starting:
                
                starting = vocab[value] + 1
            
            else:
                longest = max(longest, index - starting + 1)
                
            vocab[value] = index
            
            
        return longest