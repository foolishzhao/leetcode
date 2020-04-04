from typing import List


class SearchTreeNode:
    def __init__(self, val: int):
        self.val = val
        self.count = 1
        self.leftSize = 0
        self.left = None
        self.right = None


class SearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val: int):
        if not self.root:
            self.root = SearchTreeNode(val)
            return

        cur = self.root
        while cur:
            if val == cur.val:
                cur.count += 1
                return
            elif val < cur.val:
                cur.leftSize += 1
                if not cur.left:
                    cur.left = SearchTreeNode(val)
                    return
                else:
                    cur = cur.left
            else:
                if not cur.right:
                    cur.right = SearchTreeNode(val)
                    return
                else:
                    cur = cur.right

    def countLessEqThan(self, val: int) -> int:
        return self._countLessEqThan(self.root, val)

    def _countLessEqThan(self, root: SearchTreeNode, val: int) -> int:
        if not root:
            return 0

        if val == root.val:
            return root.count + root.leftSize
        elif val < root.val:
            return self._countLessEqThan(root.left, val)
        else:
            return root.leftSize + root.count + self._countLessEqThan(root.right, val)


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

    def sumRange(self, i: int, j: int) -> int:
        return self.sumPrefix(j) - self.sumPrefix(i - 1)


class SegmentTreeNode:
    def __init__(self, begin: int, end: int):
        self.begin = begin
        self.end = end
        self.val = 0
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, n: int):
        self.root = self._build(0, n - 1)

    def _build(self, begin: int, end: int) -> SegmentTreeNode:
        if begin > end:
            return None
        elif begin == end:
            return SegmentTreeNode(begin, end)
        else:
            root = SegmentTreeNode(begin, end)

            mid = (end - begin) // 2 + begin
            root.left = self._build(begin, mid)
            root.right = self._build(mid + 1, end)

            return root

    def update(self, i: int, delta: int):
        return self._update(self.root, i, delta)

    def _update(self, root: SegmentTreeNode, i: int, delta: int):
        if root.begin == root.end:
            root.val += delta
            return

        if root.left.end >= i:
            self._update(root.left, i, delta)
        else:
            self._update(root.right, i, delta)

        root.val = root.left.val + root.right.val

    def sumRange(self, i: int, j: int) -> int:
        return self._sumRange(self.root, i, j)

    def _sumRange(self, root: SegmentTreeNode, i: int, j: int) -> int:
        if not root:
            return 0

        if root.end < i or j < root.begin:
            return 0

        if i <= root.begin and root.end <= j:
            return root.val

        return self._sumRange(root.left, i, j) + self._sumRange(root.right, i, j)


class Solution:
    # search tree
    # Time Limit Exceeded
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sumNums = [0] * (n + 1)
        for i in range(n):
            sumNums[i + 1] = sumNums[i] + nums[i]

        st = SearchTree()
        res = 0
        for i in range(n):
            st.insert(sumNums[i])
            res += st.countLessEqThan(sumNums[i + 1] - lower) - st.countLessEqThan(sumNums[i + 1] - upper - 1)

        return res

    # binary index tree
    def countRangeSum2(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sumNums = [0] * (n + 1)
        for i in range(n):
            sumNums[i + 1] = sumNums[i] + nums[i]

        sortedSumNums = sorted(set(sumNums))
        dt = {num: i for i, num in enumerate(sortedSumNums)}
        bit = BinaryIndexTree(len(dt))

        res, sortedN = 0, len(dt)
        for i in range(n):
            idx = dt[sumNums[i]]
            bit.update(idx, 1)

            left = self.searchGreatEq(sortedSumNums, sumNums[i + 1] - upper)
            right = self.searchLessEq(sortedSumNums, sumNums[i + 1] - lower)
            if left != -1 and right != -1:
                res += bit.sumRange(left, right)

        return res

    # segment tree
    def countRangeSum3(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sumNums = [0] * (n + 1)
        for i in range(n):
            sumNums[i + 1] = sumNums[i] + nums[i]

        sortedSumNums = sorted(set(sumNums))
        dt = {num: i for i, num in enumerate(sortedSumNums)}
        st = SegmentTree(len(dt))

        res, sortedN = 0, len(dt)
        for i in range(n):
            idx = dt[sumNums[i]]
            st.update(idx, 1)

            left = self.searchGreatEq(sortedSumNums, sumNums[i + 1] - upper)
            right = self.searchLessEq(sortedSumNums, sumNums[i + 1] - lower)
            if left != -1 and right != -1:
                res += st.sumRange(left, right)

        return res

    def searchGreatEq(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] >= val:
                if mid == left or nums[mid - 1] < val:
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def searchLessEq(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] <= val:
                if mid == right or nums[mid + 1] > val:
                    return mid
                left = mid + 1
            else:
                right = mid - 1

        return -1

    # merge sort
    def countRangeSum4(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sumNums = [0] * (n + 1)
        for i in range(n):
            sumNums[i + 1] = sumNums[i] + nums[i]

        return self.mergeSort(sumNums, 0, n, lower, upper)

    def mergeSort(self, nums: List[int], left: int, right: int, lower: int, upper: int) -> int:
        if left >= right:
            return 0

        res = 0
        mid = (right - left) // 2 + left
        res += self.mergeSort(nums, left, mid, lower, upper)
        res += self.mergeSort(nums, mid + 1, right, lower, upper)

        t = list()
        i, j, u, v = left, mid + 1, mid + 1, mid + 1
        while i <= mid:
            while u <= right and lower + nums[i] > nums[u]:
                u += 1
            while v <= right and nums[v] <= upper + nums[i]:
                v += 1
            while j <= right and nums[j] <= nums[i]:
                t.append(nums[j])
                j += 1
            t.append(nums[i])
            res += v - u
            i += 1

        for i, v in enumerate(t):
            nums[left + i] = v

        return res
