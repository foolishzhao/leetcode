from python3.common.define import TreeNode


class Solution:
    def __init__(self):
        self.greatSum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            root.val += self.greatSum
            self.greatSum = root.val
            self.bstToGst(root.left)
        return root
