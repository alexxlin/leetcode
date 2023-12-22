class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        largest = 1
        d = {}
        start, end = 0, 0
        for i, char in enumerate(s):
            if char in d and d[char] >= start:
                start = d[char] + 1
            end = i
            largest = max(largest, end - start + 1)
            d[char] = i
        
        return largest
