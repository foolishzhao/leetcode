from typing import List
import bisect


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SearchTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, cur, x):
        if not cur:
            return TreeNode(x)

        if x < cur.val:
            cur.left = self._insert(cur.left, x)
        else:
            cur.right = self._insert(cur.right, x)

        return cur

    # first val >= x
    def search(self, x):
        cur, res = self.root, -1
        while cur:
            if x < cur.val:
                res = cur.val
                cur = cur.left
            elif x == cur.val:
                return x
            else:
                cur = cur.right

        return res


# Time Limit Exceeded
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n, res = len(matrix), len(matrix[0]), float('-inf')
        for i in range(n):
            subArr = [0] * m
            for j in range(i, n):
                for t in range(m):
                    subArr[t] += matrix[t][j]
                res = max(res, self.maxSumSubarray(subArr, k))

        return res

    def maxSumSubarray(self, nums, k):
        st = SearchTree()
        st.insert(0)

        curSum, res = 0, float('-inf')
        for num in nums:
            curSum += num
            t = st.search(curSum - k)
            if t != -1:
                res = max(res, curSum - t)
            st.insert(curSum)

        return res


class Solution2:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n, res = len(matrix), len(matrix[0]), float('-inf')
        for i in range(n):
            subArr = [0] * m
            for j in range(i, n):
                for t in range(m):
                    subArr[t] += matrix[t][j]
                res = max(res, self.maxSumSubarray(subArr, k))

        return res

    def maxSumSubarray(self, nums, k):
        cur, res = 0, float('-inf')
        sums = [0]

        for i in range(1, len(nums) + 1):
            cur += nums[i - 1]
            idx = bisect.bisect_left(sums, cur - k)
            if idx != i:
                res = max(res, cur - sums[idx])
            # O(n) time complexity
            bisect.insort(sums, cur)

        return res


if __name__ == '__main__':
    print(Solution().maxSumSubmatrix([
        [5, -4, -3, 4],
        [-3, -4, 4, 5],
        [5, 1, 5, -4],
    ], 10))
