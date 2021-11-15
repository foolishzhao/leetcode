from python3.common.define import TreeNode
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.left:
            return self.minDepth(root.right) + 1

        if not root.right:
            return self.minDepth(root.left) + 1

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
