class MinStack:
    # maintain the stack and also the current minimum
    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack:
            current_min = self.getMin()
            new_min = min(current_min, val)
            self.stack.append((val, new_min))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
