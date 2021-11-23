from typing import Optional

#O(n)
from python3.common.define import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

class Solution:
    def getHeight(self, root):
        if not root:
            return 0
        return 1 + self.getHeight(root.left)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        heightLeft = self.getHeight(root.left)
        heightRight = self.getHeight(root.right)
        if heightLeft == heightRight:
            return pow(2, heightLeft) + self.countNodes(root.right)
        else:
            return pow(2, heightRight) + self.countNodes(root.left)