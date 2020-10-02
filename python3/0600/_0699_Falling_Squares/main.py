from typing import List


class SegmentTreeNode:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.val = 0
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, n):
        self.root = self._build(0, n - 1)

    def _build(self, begin, end):
        if begin > end:
            return None
        elif begin == end:
            return SegmentTreeNode(begin, end)
        else:
            mi = (end - begin) // 2 + begin
            root = SegmentTreeNode(begin, end)
            root.left = self._build(begin, mi)
            root.right = self._build(mi + 1, end)
            return root

    def updateRange(self, begin, end, val):
        self._updateRange(self.root, begin, end, val)

    def _updateRange(self, root, begin, end, val):
        if not root or begin > root.end or end < root.begin:
            return

        root.val = max(root.val, val)
        self._updateRange(root.left, begin, end, val)
        self._updateRange(root.right, begin, end, val)

    def maxRange(self, begin, end):
        return self._maxRange(self.root, begin, end)

    def _maxRange(self, root, begin, end):
        if not root or begin > root.end or end < root.begin:
            return 0

        if begin <= root.begin and root.end <= end:
            return root.val

        return max(self._maxRange(root.left, begin, end), self._maxRange(root.right, begin, end))


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        def getHeight(left, right):
            res = 0
            for l, r, h in intervals:
                if left >= r or right <= l:
                    continue
                res = max(res, h)
            return res

        res, maxH, intervals = list(), 0, list()
        for l, h in positions:
            r = l + h
            curH = getHeight(l, r) + h
            intervals.append([l, r, curH])
            maxH = max(maxH, curH)
            res.append(maxH)
        return res

    def fallingSquares2(self, positions: List[List[int]]) -> List[int]:
        posSet = set()
        for b, l in positions:
            posSet.add(b)
            posSet.add(b + l - 1)  # minus one here to avoid get stuck prematurely
        posIndex = {pos: i for i, pos in enumerate(sorted(list(posSet)))}

        st = SegmentTree(len(posIndex))
        res, maxH = list(), 0
        for b, l in positions:
            begin, end = posIndex[b], posIndex[b + l - 1]
            h = st.maxRange(begin, end) + l
            maxH = max(maxH, h)
            res.append(maxH)
            st.updateRange(begin, end, h)
        return res
