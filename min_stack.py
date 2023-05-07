class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if self.min_stack:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
        
        # self.stack.append(val)
        # val = min(val, self.min_stack[-1] if self.min_stack else val)
        # self.min_stack.append(val)
    
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]