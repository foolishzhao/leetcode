from python3.common.define import TreeNode


class Solution:
    def __init__(self):
        self.res = float('inf')
        self.prev = float('-inf')

    def getMinimumDifference(self, root: TreeNode) -> int:
        if root:
            self.getMinimumDifference(root.left)
            self.res = min(self.res, root.val - self.prev)
            self.prev = root.val
            self.getMinimumDifference(root.right)
        return self.res
