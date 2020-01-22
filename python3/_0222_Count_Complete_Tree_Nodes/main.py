from python3.common.define import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftCount, rightCount = 0, 0

        cur = root
        while cur:
            leftCount += 1
            cur = cur.left

        cur = root
        while cur:
            rightCount += 1
            cur = cur.right

        if leftCount == rightCount:
            return 2 ** leftCount - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
