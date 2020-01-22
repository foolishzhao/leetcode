from typing import List


class SearchTreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class SearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    # note how to handle equal val, treat them as > root val
    def _insert(self, root: SearchTreeNode, val: int) -> SearchTreeNode:
        if not root:
            return SearchTreeNode(val)

        if val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)
        return root

    def delete(self, val):
        cur, curP = self.root, None
        while cur:
            if val == cur.val:
                break
            elif val < cur.val:
                curP, cur = cur, cur.left
            else:
                curP, cur = cur, cur.right

        if cur.left and cur.right:
            t, tp = cur.right, cur
            while t.left:
                tp, t = t, t.left
            # don't forget to replace cur' val with t' val
            cur.val = t.val
            curP, cur = tp, t

        child = None
        if cur.left:
            child = cur.left
        elif cur.right:
            child = cur.right

        if not curP:
            self.root = child
        elif curP.left == cur:
            curP.left = child
        else:
            curP.right = child

    def searchMax(self) -> int:
        cur = self.root
        while cur.right:
            cur = cur.right

        return cur.val


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        deque = list()
        for i, v in enumerate(nums):
            while deque and v >= deque[-1][1]:
                deque.pop()
            deque.append((i, v))

            if i >= k and deque[0][0] == i - k:
                deque.pop(0)

            if i >= k - 1:
                res.append(deque[0][1])

        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        res = []

        st = SearchTree()
        for i, v in enumerate(nums):
            st.insert(v)
            if i >= k:
                st.delete(nums[i - k])
            if i >= k - 1:
                res.append(st.searchMax())

        return res


if __name__ == '__main__':
    Solution().maxSlidingWindow2([1, 3, -1, -3, 5, 3, 6, 7], 3)
