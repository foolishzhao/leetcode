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

    def countLess(self, val: int) -> int:
        return self._countLess(self.root, val)

    def _countLess(self, root: SearchTreeNode, val: int) -> int:
        if not root:
            return 0

        if val == root.val:
            return root.leftSize
        elif val < root.val:
            return self._countLess(root.left, val)
        else:
            return root.leftSize + root.count + self._countLess(root.right, val)


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
            mid = (end - begin) // 2 + begin

            root = SegmentTreeNode(begin, end)
            root.left = self._build(begin, mid)
            root.right = self._build(mid + 1, end)
            root.val = root.left.val + root.right.val

            return root

    def update(self, i: int, delta: int):
        self._update(self.root, i, delta)

    def _update(self, root: SegmentTreeNode, i: int, delta: int):
        if root.begin == root.end:
            root.val += delta
            return

        if i <= root.left.end:
            self._update(root.left, i, delta)
        else:
            self._update(root.right, i, delta)

        root.val = root.left.val + root.right.val

    def sumRange(self, i: int, j: int) -> int:
        return self._sumRange(self.root, i, j)

    def _sumRange(self, root: SegmentTreeNode, i: int, j: int) -> int:
        if not root:
            return 0

        if root.end < i or root.begin > j:
            return 0

        if i <= root.begin and root.end <= j:
            return root.val

        return self._sumRange(root.left, i, j) + self._sumRange(root.right, i, j)


class Solution:
    # merge sort
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return 0

        res = 0
        mid = (right - left) // 2 + left
        res += self.mergeSort(nums, left, mid)
        res += self.mergeSort(nums, mid + 1, right)

        t = list()
        i, j, k = mid, right, right
        while i >= left:
            while k > mid and nums[i] <= 2 * nums[k]:
                k -= 1
            res += k - mid

            while j > mid and nums[j] >= nums[i]:
                t.append(nums[j])
                j -= 1
            t.append(nums[i])
            i -= 1

        while j > mid:
            t.append(nums[j])
            j -= 1

        t = t[::-1]
        for i, v in enumerate(t):
            nums[left + i] = v

        return res

    # Time Limited Exceeded
    # search tree
    def reversePairs2(self, nums: List[int]) -> int:
        st = SearchTree()
        res = 0
        for num in nums[::-1]:
            if num % 2 == 0:
                res += st.countLess(num // 2)
            else:
                res += st.countLess(num // 2 + 1)
            st.insert(num)

        return res

    # binary index tree
    def reversePairs3(self, nums: List[int]) -> int:
        sortedNums = sorted(set(nums))
        dt = {num: i for i, num in enumerate(sortedNums)}

        res, n = 0, len(dt)
        bit = BinaryIndexTree(n)
        for num in nums[::-1]:
            idx = -1
            if num % 2 == 0:
                idx = self.searchLess(sortedNums, num // 2)
            else:
                idx = self.searchLess(sortedNums, num // 2 + 1)
            if idx != -1:
                res += bit.sumPrefix(idx)

            bit.update(dt[num], 1)

        return res

    # Time Limited Exceeded\
    # segment tree
    def reversePairs4(self, nums: List[int]) -> int:
        sortedNums = sorted(set(nums))
        dt = {num: i for i, num in enumerate(sortedNums)}

        res, n = 0, len(dt)
        st = SegmentTree(n)
        for num in nums[::-1]:
            idx = -1
            if num % 2 == 0:
                idx = self.searchLess(sortedNums, num // 2)
            else:
                idx = self.searchLess(sortedNums, num // 2 + 1)
            if idx != -1:
                res += st.sumRange(0, idx)

            st.update(dt[num], 1)

        return res

    def searchLess(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < val:
                if mid == right or nums[mid + 1] >= val:
                    return mid
                left = mid + 1
            else:
                right = mid - 1

        return -1
