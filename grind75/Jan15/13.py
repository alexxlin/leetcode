class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 
100, 'D': 500, 'M': 1000}
        subtraction = {'I': ['V', 'X'], 'X': ['L', 'C'], 
'C': ['D', 'M']}

        n = len(s)
        result = 0
        for i, char in enumerate(s):
            if i != n-1 and char in subtraction and s[i+1] 
in subtraction[char]:
                result -= mapping[char]
            else:
                result += mapping[char]
        return result
