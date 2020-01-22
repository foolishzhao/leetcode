from typing import List


class SegmentTreeNode:
    def __init__(self, begin: int, end: int, val: int):
        self.begin = begin
        self.end = end
        self.val = val
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, n):
        self.root = self._build(0, n - 1)

    def _build(self, begin: int, end: int):
        if begin > end:
            return None
        elif begin == end:
            return SegmentTreeNode(begin, end, 0)
        else:
            mid = (end - begin) // 2 + begin

            root = SegmentTreeNode(begin, end, 0)
            root.left = self._build(begin, mid)
            root.right = self._build(mid + 1, end)

            root.val = root.left.val + root.right.val
            return root

    def update(self, i: int, diff: int):
        return self._update(self.root, i, diff)

    def _update(self, root: SegmentTreeNode, i: int, diff: int):
        if root.begin == root.end:
            if i == root.begin:
                root.val += diff
            return
        if root.left.end >= i:
            self._update(root.left, i, diff)
        else:
            self._update(root.right, i, diff)
        root.val = root.left.val + root.right.val

    def sumRange(self, i: int, j: int) -> int:
        return self._sumRange(self.root, i, j)

    def _sumRange(self, root: SegmentTreeNode, i: int, j: int) -> int:
        if root.end < i or j < root.begin:
            return 0
        if i <= root.begin and root.end <= j:
            return root.val
        return self._sumRange(root.left, i, j) + self._sumRange(root.right, i, j)


class SearchTreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.leftSize = 0
        self.count = 1


class SearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val: int) -> int:
        if not self.root:
            self.root = SearchTreeNode(val)
            return 0

        return self._insert(self.root, val)

    def _insert(self, root: SearchTreeNode, val: int) -> int:
        if val == root.val:
            root.count += 1
            return root.leftSize
        elif val < root.val:
            root.leftSize += 1
            if not root.left:
                root.left = SearchTreeNode(val)
                return 0
            else:
                return self._insert(root.left, val)
        else:
            if not root.right:
                root.right = SearchTreeNode(val)
                return root.leftSize + root.count
            else:
                return root.leftSize + root.count + self._insert(root.right, val)


class BinaryIndexTree:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n + 1)

    def update(self, i: int, delta: int):
        i += 1
        while i <= self.n:
            self.arr[i] += delta
            i += i & -i

    def sumPrefix(self, i: int) -> int:
        i += 1
        res = 0
        while i:
            res += self.arr[i]
            i -= i & -i

        return res


class Solution:
    # The smaller numbers on the right of a number are exactly those that jump from its right to its left
    # during a stable sort. So can do merge sort with added tracking of those right-to-left jumps.
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = [0] * len(nums)
        self.mergeSort(res, list(enumerate(nums)))
        return res

    def mergeSort(self, res, nums):
        mid = len(nums) // 2
        if mid:
            left = self.mergeSort(res, nums[:mid])
            right = self.mergeSort(res, nums[mid:])
            i = len(nums) - 1
            while left or right:
                if not right or left and left[-1][1] > right[-1][1]:
                    res[left[-1][0]] += len(right)
                    nums[i] = left.pop()
                else:
                    nums[i] = right.pop()
                i -= 1

        return nums

    # segment tree
    def countSmaller2(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        dt = {num: idx for idx, num in enumerate(sorted(list(set(nums))))}

        n = len(nums)
        st = SegmentTree(n)

        res = [0] * n
        for i in range(n - 1, -1, -1):
            idx = dt[nums[i]]
            res[i] = st.sumRange(0, idx - 1)
            st.update(idx, 1)

        return res

    # search tree
    def countSmaller3(self, nums: List[int]) -> List[int]:
        st = SearchTree()

        res = list()
        for num in nums[::-1]:
            res.append(st.insert(num))

        return res[::-1]

    # binary index tree
    def countSmaller4(self, nums: List[int]) -> List[int]:
        dt = {num: i for i, num in enumerate(sorted(set(nums)))}
        bit = BinaryIndexTree(len(nums))

        res = list()
        for num in nums[::-1]:
            idx = dt[num]
            res.append(bit.sumPrefix(idx - 1))
            bit.update(idx, 1)

        return res[::-1]


if __name__ == '__main__':
    Solution().countSmaller3([5, 2, 6, 1])
