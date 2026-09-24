class MyStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        n=len(self.stack)
        for i in range(n-1):
            self.stack.append(self.stack.pop(0))


    def pop(self) -> int:
        if len(self.stack)==0:
            print("underflow")
        return self.stack.pop(0)        
    def top(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return len(self.stack)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()