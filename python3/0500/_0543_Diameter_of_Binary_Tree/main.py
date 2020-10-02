from python3.common.define import TreeNode


class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        ld = self.dfs(root.left)
        rd = self.dfs(root.right)
        self.res = max(self.res, ld + rd)
        return max(ld, rd) + 1
