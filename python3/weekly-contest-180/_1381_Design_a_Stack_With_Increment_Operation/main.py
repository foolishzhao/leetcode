class CustomStack:

    def __init__(self, maxSize: int):
        self.st = list()
        self.cap = maxSize

    def push(self, x: int) -> None:
        if len(self.st) < self.cap:
            self.st.append(x)

    def pop(self) -> int:
        if self.st:
            return self.st.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.st), k)):
            self.st[i] += val


class CustomStack2:

    def __init__(self, maxSize: int):
        self.st = list()
        self.n = maxSize
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.st) < self.n:
            self.st.append(x)

    def pop(self) -> int:
        if not self.st:
            return -1

        i = len(self.st) - 1
        inc = self.inc[i]
        if i:
            self.inc[i - 1] += inc
        self.inc[i] = 0

        return self.st.pop() + inc

    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.st)) - 1
        if i >= 0:
            self.inc[i] += val
