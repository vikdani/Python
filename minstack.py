# define a stack and do push , pop ,peak and min operation.
class Minstack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self,val):
        self.stack.append(val)
        if not self.minstack or val<=self.minstack[-1]:
            self.minstack.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1]==self.minstack[-1]:
                self.minstack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        if self.minstack:
            return self.minstack[-1]
        
                              
        
