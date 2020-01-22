class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1 = list()
        self.st2 = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st2.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.st1:
            while self.st2:
                self.st1.append(self.st2.pop())

        return self.st1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.st1:
            while self.st2:
                self.st1.append(self.st2.pop())

        return self.st1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.st1 and not self.st2
