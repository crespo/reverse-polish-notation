class Stack:
    def __init__(self):
        self.stack = []
        
    
    def push(self, value):
        self.stack.append(value)
    
    
    def pop(self):
        return self.stack.pop()
    
    
    def size(self):
        return len(self.stack)
    
    
    def toString(self): 
        if not self.stack:
            print("Stack is empty.")
        else:
            s = self.stack.copy().reverse()
            n = len(s) - 1
            for e in s:    
                print(f"level: {n} | operand:  {e}")
                n -= 1