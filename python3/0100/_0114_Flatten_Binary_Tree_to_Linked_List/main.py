from python3.common.define import TreeNode
from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        leftRes, rightRes = root.left, root.right
        root.left = None
        if leftRes:
            root.right = leftRes
            while leftRes.right:
                leftRes = leftRes.right
            leftRes.right = rightRes
        else:
            root.right = rightRes
