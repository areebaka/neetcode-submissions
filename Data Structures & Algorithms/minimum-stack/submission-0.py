class MinStack:

    def __init__(self):
        self.actualStack = []  
        self.minStack = []

    def push(self, val: int) -> None:
        self.actualStack.append(val)
        if self.minStack:
            val= min(val,self.minStack[-1])
        self.minStack.append(val)
    

    def pop(self) -> None:
        self.actualStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.actualStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
