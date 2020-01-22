# dynamic max segment tree
# range query
# range update


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
