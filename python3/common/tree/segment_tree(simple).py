from typing import List


class TreeNode:
    def __init__(self, begin: int, end: int, val: int):
        self.begin = begin
        self.end = end
        self.val = val
        self.left = None
        self.right = None


# sum segment tree
# range query
# single index update
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


if __name__ == '__main__':
    st = SegmentTree([4, 6, 3, 5, 8, 2, 1])
    print(st.sumRange(0, 0))
    print(st.sumRange(0, 3))
    st.update(0, 1)
    print(st.sumRange(0, 0))
