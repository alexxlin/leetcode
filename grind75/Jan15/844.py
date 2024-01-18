class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(text):
            stack = []
            for char in text:
                if char == '#' and stack:
                    stack.pop()
                if char != '#':
                    stack.append(char)
            return stack
        
        return helper(s) == helper(t)
