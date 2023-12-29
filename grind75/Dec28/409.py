from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        result = 0
        has_odd = False
        for key in c:
            if c[key] % 2 == 0:
                result += c[key]
            else:
                has_odd = True
                result += c[key] - 1
        
        if has_odd:
            return result + 1
        return result
