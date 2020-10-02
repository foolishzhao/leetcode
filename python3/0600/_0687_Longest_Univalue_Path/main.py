from python3.common.define import TreeNode


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res, _ = self.dfs(root)
        return res

    def dfs(self, root):
        if not root:
            return 0, 0

        lr, lp = self.dfs(root.left)
        if not (root.left and root.val == root.left.val):
            lp = 0

        rr, rp = self.dfs(root.right)
        if not (root.right and root.val == root.right.val):
            rp = 0

        return max(lr, rr, lp + rp), 1 + max(lp, rp)
