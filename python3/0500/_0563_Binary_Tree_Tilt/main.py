from python3.common.define import TreeNode


class Solution:
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.tilt

    def dfs(self, root):
        if not root:
            return 0

        lr = self.dfs(root.left)
        rr = self.dfs(root.right)
        self.tilt += abs(lr - rr)
        return lr + rr + root.val
