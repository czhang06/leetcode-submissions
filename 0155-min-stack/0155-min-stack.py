class MinStack:

    def __init__(self):
        self.stack = []
        self.msf = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.msf:
            self.msf.append(value)
        else:
            self.msf.append(min(self.msf[-1], value))

    def pop(self) -> None:
        self.stack.pop()
        self.msf.pop()

            
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.msf[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()