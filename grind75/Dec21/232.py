class MyQueue:

    # for every push, push into side stack and push back into main stack, 
LIFO + LIFO = FIFO

    def __init__(self):
        self.main_stack = []
        self.side_stack = []


    def push(self, x: int) -> None:
        for _ in range(len(self.main_stack)):
            self.side_stack.append(self.main_stack.pop())
        self.side_stack.append(x)

        for _ in range(len(self.side_stack)):
            self.main_stack.append(self.side_stack.pop())


    def pop(self) -> int:
        return self.main_stack.pop()

    def peek(self) -> int:
        return self.main_stack[-1]
        
        

    def empty(self) -> bool:
        return not self.main_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
