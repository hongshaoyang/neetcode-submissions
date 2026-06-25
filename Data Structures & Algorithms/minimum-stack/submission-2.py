from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
        

    def push(self, val: int) -> None:
        x = None
        if len(self.stack) == 0 or val < self.getMin():
            x = val
        else:
            x = self.getMin()

        self.min_stack.append(x)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
