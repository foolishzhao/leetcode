class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = list()
        self.last = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        self.last = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        t = list()
        while len(self.q) > 1:
            cur = self.q.pop(0)
            t.append(cur)
            self.last = cur

        res = self.q.pop()
        self.q = t
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.last

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q
