from typing import List


class TreeNode:
    def __init__(self, begin: int, end: int, val: int):
        self.begin = begin
        self.end = end
        self.val = val
        self.left = None
        self.right = None


class BinaryIndexTree:
    def __init__(self, nums: List[int]):
        nums = nums.copy()
        n = len(nums)
        nums.insert(0, 0)
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j <= n:
                nums[j] += nums[i]

        self.n = n
        self.arr = nums

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

    def sumRange(self, i: int, j: int) -> int:
        return self.sumPrefix(j) - self.sumPrefix(i - 1)


class NumArray:

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
            root.val = root.left.val + root.right.val

            return root

    def update(self, i: int, val: int) -> None:
        self._update(self.root, i, val)

    def _update(self, root: TreeNode, i: int, val: int) -> None:
        if root.begin == root.end:
            if i == root.begin:
                root.val = val
            return
        else:
            if i <= root.left.end:
                self._update(root.left, i, val)
            else:
                self._update(root.right, i, val)
            root.val = root.left.val + root.right.val

    def sumRange(self, i: int, j: int) -> int:
        return self._sumRange(self.root, i, j)

    def _sumRange(self, root: TreeNode, i: int, j: int) -> int:
        if j < root.begin or i > root.end:
            return 0

        if root.begin >= i and root.end <= j:
            return root.val

        return self._sumRange(root.left, i, j) + self._sumRange(root.right, i, j)


class NumArray2:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BinaryIndexTree(nums)

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.nums[i] = val
        self.bit.update(i, delta)

    def sumRange(self, i: int, j: int) -> int:
        return self.bit.sumRange(i, j)
