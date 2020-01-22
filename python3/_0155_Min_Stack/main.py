class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.minSt = []

    def push(self, x: int) -> None:
        self.st.append(x)
        if not self.minSt or self.minSt[-1] >= x:
            self.minSt.append(x)

    def pop(self) -> None:
        if self.st:
            cur = self.st.pop()
            if cur == self.minSt[-1]:
                self.minSt.pop()

    def top(self) -> int:
        return self.st[-1] if self.st else None

    def getMin(self) -> int:
        return self.minSt[-1] if self.minSt else None
