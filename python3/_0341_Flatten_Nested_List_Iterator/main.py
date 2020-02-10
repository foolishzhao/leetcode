class NestedInteger(object):
    pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self._putToStack(nestedList, self.stack)

    def _putToStack(self, nestedList, stack):
        for v in nestedList[::-1]:
            if v.isInteger():
                stack.append(v.getInteger())
            else:
                self._putToStack(v.getList(), stack)

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return self.stack


class NestedIterator2:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        if self.hasNext():
            return self.stack.pop()
        return None

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            self.stack = self.stack[:-1] + self.stack[-1].getList()[::-1]
        return self.stack
