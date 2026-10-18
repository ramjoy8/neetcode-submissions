class MinStack:

    def __init__(self):
        self.list_stack = []
        self.min_stack = None
        

    def push(self, val: int) -> None:

        if self.min_stack is not None and  val <= self.min_stack:
            self.list_stack.append(val + val - self.min_stack)
            self.min_stack = val
        else:
            self.list_stack.append(val)
            if self.min_stack is None:
                self.min_stack = val


    def pop(self) -> None:
        if not self.list_stack:
            return None
        val = self.list_stack.pop()
        if val < self.min_stack:
            self.min_stack = self.min_stack + self.min_stack - val

        if not self.list_stack:
            self.min_stack = None

    def top(self) -> int:
        if not self.list_stack:
            return None
        val = self.list_stack[-1]
        if val < self.min_stack:
            return self.min_stack 
        else:
            return val

    def getMin(self) -> int:
        return self.min_stack
