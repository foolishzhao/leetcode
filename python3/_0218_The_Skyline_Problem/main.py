import heapq
from typing import List


class TreeNode:
    def __init__(self, begin: int, end: int, val: int):
        self.begin = begin
        self.end = end
        self.val = val
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = self._build(0, len(nums) - 1, nums)

    def _build(self, begin: int, end: int, nums: List[int]) -> TreeNode:
        if begin > end:
            return None
        elif begin == end:
            return TreeNode(begin, end, nums[begin])
        else:
            mid = (end - begin) // 2 + begin

            root = TreeNode(begin, end, 0)
            root.left = self._build(begin, mid, nums)
            root.right = self._build(mid + 1, end, nums)
            root.val = max(root.left.val, root.right.val)

            return root

    def maxRange(self, i: int, j: int) -> int:
        return self._maxRange(self.root, i, j)

    def _maxRange(self, root: TreeNode, i: int, j: int) -> int:
        if j < root.begin or i > root.end:
            return 0

        if i <= root.begin and root.end <= j:
            return root.val

        return max(self._maxRange(root.left, i, j), self._maxRange(root.right, i, j))

    def update(self, i: int, val: int) -> None:
        self._update(self.root, i, val)

    def _update(self, root: TreeNode, i: int, val: int):
        if root.begin == root.end:
            if i == root.begin:
                root.val = val
            return
        else:
            if i <= root.left.end:
                self._update(root.left, i, val)
            else:
                self._update(root.right, i, val)
            root.val = max(root.left.val, root.right.val)


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

        res = []
        lines = list()
        for building in buildings:
            # [[0,2,3],[2,5,3]]
            # [[2,4,7],[2,4,5],[2,4,6]]
            # small x val first
            # same x val, start line prior to end line
            # same x val, highest start line first
            # same x val, lowest end line first
            heapq.heappush(lines, (building[0], -building[2]))
            heapq.heappush(lines, (building[1], building[2]))

        heights = list()
        while lines:
            x, h = heapq.heappop(lines)
            if h < 0:
                heapq.heappush(heights, h)  # note how to achieve max heap
            else:
                heights.remove(-h)
                heapq.heapify(heights)

            curHeight = 0
            if heights:
                curHeight = -heights[0]
            if not res or res[-1][1] != curHeight:
                res.append((x, curHeight))

        return res

    def getSkyline2(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

        lines = list()
        for i, building in enumerate(buildings):
            lines.append((building[0], -building[2], i))
            lines.append((building[1], building[2], i))
        heapq.heapify(lines)

        res = []
        n = len(buildings)
        # use segment tree to get cur max height
        st = SegmentTree([0] * n)
        while lines:
            x, h, idx = heapq.heappop(lines)
            if h < 0:
                st.update(idx, -h)
            else:
                st.update(idx, 0)

            curMaxHeight = st.maxRange(0, n - 1)
            if not res or curMaxHeight != res[-1][1]:
                res.append((x, curMaxHeight))

        return res


if __name__ == '__main__':
    Solution().getSkyline2([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
