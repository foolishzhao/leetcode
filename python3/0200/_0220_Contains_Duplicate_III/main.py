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

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if not root:
            return SearchTreeNode(val)

        if val == root.val:
            root.count += 1
        elif val < root.val:
            root.leftSize += 1
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)

        return root

    def delete(self, val):
        cur = self.root
        while cur:
            # mark delete
            if val == cur.val:
                cur.count -= 1
                return
            elif val < cur.val:
                cur.leftSize -= 1
                cur = cur.left
            else:
                cur = cur.right

    def searchLess(self, val) -> int:
        return self._searchLess(self.root, val)

    def _searchLess(self, root, val) -> int:
        if not root:
            return 0

        if val == root.val:
            return root.leftSize
        elif val < root.val:
            return self._searchLess(root.left, val)
        else:
            return root.leftSize + root.count + self._searchLess(root.right, val)


class Solution:
    # search tree
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # corner case
        if t < 0:
            return False

        st = SearchTree()
        for i, num in enumerate(nums):
            if i > k:
                st.delete(nums[i - k - 1])

            if i > 0:
                if st.searchLess(num + t + 1) != st.searchLess(num - t):
                    return True

            st.insert(num)

        return False

    # bucket
    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        bucket = {}
        w, n = t + 1, len(nums)
        for i, num in enumerate(nums):
            b = num // w
            if b in bucket:
                return True
            if b - 1 in bucket and abs(bucket[b - 1] - num) < w:
                return True
            if b + 1 in bucket and abs(bucket[b + 1] - num) < w:
                return True
            bucket[b] = num
            if i >= k:
                del bucket[nums[i - k] // w]

        return False


if __name__ == '__main__':
    Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
