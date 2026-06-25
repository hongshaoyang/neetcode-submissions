from collections import deque

class MinStack:

    '''
    1 2 0

    1 2 0

    1 1 0
    '''

    def __init__(self):
        self.stack = deque()
        self.prefix_stack = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # prefix approach: 

        if len(self.prefix_stack) == 0:
            self.prefix_stack.append(val)
        else:
            prefix_min = min(val, self.prefix_stack[-1])
            self.prefix_stack.append(prefix_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.prefix_stack.pop()
        

    def top(self) -> int:
        '''
        get top element aka peek
        '''
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.prefix_stack[-1]

        
