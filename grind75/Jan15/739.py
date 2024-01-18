class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> 
List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, temp])
        return result
