class MyQueue:

    def __init__(self):
        self.stack = []
        self.second = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if not self.second:
            while self.stack:
                self.second.append(self.stack.pop())
            return self.second.pop()
        return self.second.pop()
        

    def peek(self) -> int:
        if not self.second:
            return self.stack[0]
        return self.second[-1]
        

    def empty(self) -> bool:
        return not self.second and not self.stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()