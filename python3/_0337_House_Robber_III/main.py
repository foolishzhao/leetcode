from python3.common.define import TreeNode


class Solution:
    # dfs, Time Limit Exceeded
    def rob(self, root: TreeNode) -> int:
        return self.dfs(root, True)

    def dfs(self, root, canRob):
        if not root:
            return 0

        # do not rob
        r1 = self.dfs(root.left, True) + self.dfs(root.right, True)
        r2 = 0
        if canRob:
            r2 = root.val + self.dfs(root.left, False) + self.dfs(root.right, False)

        return max(r1, r2)

    # dfs with memorization
    def rob2(self, root: TreeNode) -> int:
        return self.dfs(root, True, dict())

    def dfs(self, root, canRob, dt):
        if not root:
            return 0

        if (root, canRob) in dt:
            return dt[(root, canRob)]

        # case 1: do not rob
        res = self.dfs(root.left, True, dt) + self.dfs(root.right, True, dt)
        # case 2: rob
        if canRob:
            res = max(res, root.val + self.dfs(root.left, False, dt) + self.dfs(root.right, False, dt))

        dt[(root, canRob)] = res
        return res
