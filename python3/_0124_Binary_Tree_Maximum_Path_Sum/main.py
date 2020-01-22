from python3.common.define import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        _, res = self.maxPathSumHelper(root)
        return res

    def maxPathSumHelper(self, root: TreeNode) -> (int, int):
        if not root:
            return -(1 << 31), -(1 << 31)

        lSingle, lRes = self.maxPathSumHelper(root.left)
        rSingle, rRes = self.maxPathSumHelper(root.right)

        curRes = root.val
        if lSingle > 0:
            curRes += lSingle
        if rSingle > 0:
            curRes += rSingle

        return root.val + max(0, lSingle, rSingle), max(lRes, curRes, rRes)
