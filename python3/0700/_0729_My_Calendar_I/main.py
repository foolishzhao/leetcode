class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        if start >= end:
            return False

        cur = (start, end)

        if not self.intervals or self.intervals[-1][1] <= cur[0]:
            self.intervals.append(cur)
            return True
        elif cur[1] <= self.intervals[0][0]:
            self.intervals.insert(0, cur)
            return True

        i, n = 0, len(self.intervals)
        while i < n and self.intervals[i][0] <= cur[0]:
            i += 1

        if i == 0 or i == n:
            return False

        if cur[0] >= self.intervals[i - 1][1] and cur[1] <= self.intervals[i][0]:
            self.intervals.insert(i, cur)
            return True

        return False


class SearchTreeNode:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class SearchTree:
    def __init__(self):
        self.root = None

    def insert(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = SearchTreeNode(start, end)
            return True

        cur = self.root
        while cur:
            if cur.start >= end:
                if not cur.left:
                    cur.left = SearchTreeNode(start, end)
                    return True
                else:
                    cur = cur.left
            elif cur.end <= start:
                if not cur.right:
                    cur.right = SearchTreeNode(start, end)
                    return True
                else:
                    cur = cur.right
            else:
                return False


class MyCalendar2:

    def __init__(self):
        self.st = SearchTree()

    def book(self, start: int, end: int) -> bool:
        return self.st.insert(start, end)
