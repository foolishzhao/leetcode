class SearchTreeNode:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.overlap = False
        self.left = None
        self.right = None


class SearchTree:
    def __init__(self):
        self.root = None

    def insert(self, start: int, end: int):
        if not self.root:
            self.root = SearchTreeNode(start, end)
            return

        cur = self.root
        while cur:
            if end <= cur.start:
                if not cur.left:
                    cur.left = SearchTreeNode(start, end)
                    return
                else:
                    cur = cur.left
            elif start >= cur.end:
                if not cur.right:
                    cur.right = SearchTreeNode(start, end)
                    return
                else:
                    cur = cur.right
            else:
                lStart, lEnd = min(cur.start, start), max(cur.start, start)
                rStart, rEnd = min(cur.end, end), max(cur.end, end)

                cur.start = lEnd
                cur.end = rStart
                cur.overlap = True

                self.insert(lStart, lEnd)
                self.insert(rStart, rEnd)
                return

    def canInsert(self, start: int, end: int) -> bool:
        return self._canInsert(self.root, start, end)

    def _canInsert(self, root: SearchTreeNode, start: int, end: int) -> bool:
        if not root:
            return True

        if end <= root.start:
            return self._canInsert(root.left, start, end)
        elif start >= root.end:
            return self._canInsert(root.right, start, end)
        else:
            if root.overlap:
                return False

            ls, le = min(root.start, start), max(root.start, start)
            rs, re = min(root.end, end), max(root.end, end)
            return self._canInsert(root.left, ls, le) and self._canInsert(root.right, rs, re)


class MyCalendarTwo:

    def __init__(self):
        self.st = SearchTree()

    def book(self, start: int, end: int) -> bool:
        if self.st.canInsert(start, end):
            self.st.insert(start, end)
            return True
        else:
            return False
