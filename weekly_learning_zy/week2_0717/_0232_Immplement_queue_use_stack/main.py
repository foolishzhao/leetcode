class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st2.append(x)

    def pop(self) -> int:
        if not self.st1:
            while self.st2:
                self.st1.append(self.st2.pop())
        return self.st1.pop()

    def peek(self) -> int:
        if not self.st1:
            while self.st2:
                self.st1.append(self.st2.pop())
        return self.st1[-1]

    def empty(self) -> bool:
        return not self.st1 and not self.st2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()