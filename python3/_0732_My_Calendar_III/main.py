class SearchTreeNode:
    def __init__(self, start: int, end: int, k: int):
        self.start = start
        self.end = end
        self.k = k
        self.left = None
        self.right = None


class SearchTree:
    def __init__(self):
        self.root = None
        self.k = 0

    def insert(self, start: int, end: int) -> int:
        self.root = self._insert(self.root, start, end, 1)
        return self.k

    def _insert(self, root, start: int, end: int, k: int) -> SearchTreeNode:
        if not root:
            self.k = max(self.k, k)
            return SearchTreeNode(start, end, k)

        if end <= root.start:
            root.left = self._insert(root.left, start, end, k)
        elif start >= root.end:
            root.right = self._insert(root.right, start, end, k)
        else:
            ls, le = min(root.start, start), max(root.start, start)
            lk = root.k if ls == root.start else k
            rs, re = min(root.end, end), max(root.end, end)
            rk = root.k if re == root.end else k

            root.start = le
            root.end = rs
            root.left = self._insert(root.left, ls, le, lk)
            root.right = self._insert(root.right, rs, re, rk)
            root.k += k
            self.k = max(self.k, root.k)

        return root


class MyCalendarThree:

    def __init__(self):
        self.st = SearchTree()

    def book(self, start: int, end: int) -> int:
        return self.st.insert(start, end)


class MyCalendarThree2:

    def __init__(self):
        self.timeLines = dict()

    # scan lines to find the maximum number of concurrent ongoing event at any time
    def book(self, start: int, end: int) -> int:
        self.timeLines[start] = self.timeLines.get(start, 0) + 1
        self.timeLines[end] = self.timeLines.get(end, 0) - 1

        res, cur = 0, 0
        for _, v in sorted(self.timeLines.items()):
            cur += v
            res = max(res, cur)

        return res


# optimization of MyCalendarThree2
# note: tuple value can not be updated
class MyCalendarThree3:

    def __init__(self):
        self.lines = list()

    def addLine(self, line: int, delta: int):
        left, right = 0, len(self.lines) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if self.lines[mid][0] >= line:
                if mid == left or self.lines[mid - 1][0] < line:
                    if self.lines[mid][0] == line:
                        self.lines[mid][1] += delta
                    else:
                        self.lines.insert(mid, [line, delta])
                    return
                else:
                    right = mid - 1
            else:
                left = mid + 1

        self.lines.append([line, delta])

    def book(self, start: int, end: int) -> int:
        self.addLine(start, 1)
        self.addLine(end, -1)

        res, cur = 0, 0
        for line in self.lines:
            cur += line[1]
            res = max(res, cur)

        return res


class SegmentTreeNode:
    def __init__(self, begin: int, end: int):
        self.begin = begin
        self.end = end
        self.val = 0
        self.lazy = 0
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, n):
        self.root = SegmentTreeNode(0, n - 1)

    def update(self, i: int, j: int, delta: int):
        self._update(self.root, i, j, delta)

    def _update(self, root, i, j, delta):
        if j < root.begin or i > root.end:
            return

        if i <= root.begin and root.end <= j:
            root.val += delta
            root.lazy += delta
            return

        self._pushDown(root)
        self._update(root.left, i, j, delta)
        self._update(root.right, i, j, delta)
        root.val = max(root.left.val, root.right.val)

    def _pushDown(self, root: SegmentTreeNode):
        mid = (root.end - root.begin) // 2 + root.begin
        if not root.left:
            root.left = SegmentTreeNode(root.begin, mid)

        if not root.right:
            root.right = SegmentTreeNode(mid + 1, root.end)

        root.left.val += root.lazy
        root.left.lazy += root.lazy

        root.right.val += root.lazy
        root.right.lazy += root.lazy

        root.lazy = 0

    def query(self, i: int, j: int) -> int:
        return self._query(self.root, i, j)

    def _query(self, root, i, j) -> int:
        if not root:
            return 0

        if root.end < i or j < root.begin:
            return 0

        if i <= root.begin and root.end <= j:
            return root.val

        self._pushDown(root)
        return max(self._query(root.left, i, j), self._query(root.right, i, j))


#  dynamic lazy segment tree
class MyCalendarThree4:

    def __init__(self):
        self.st = SegmentTree(10 ** 9)

    def book(self, start: int, end: int) -> int:
        self.st.update(start, end - 1, 1)
        return self.st.query(0, 10 ** 9 - 1)
