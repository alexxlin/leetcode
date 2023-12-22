import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '/':
                    stack.append(math.trunc(operand1 / operand2))
                elif token == '*':
                    stack.append(operand1 * operand2)
        
        return stack[0]
