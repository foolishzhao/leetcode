from python3.common.define import TreeNode
from typing import Optional


class Solution:
    def __init__(self):
        self.prev = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if self.prev is not None and self.prev >= root.val:
            return False
        self.prev = root.val

        if not self.isValidBST(root.right):
            return False

        return True


class Solution2:
    def isValidBST(self, root: Optional[TreeNode], lt=float('inf'), gt=float('-inf')) -> bool:
        if not root:
            return True

        if not (gt < root.val < lt):
            return False

        return self.isValidBST(root.left, root.val, gt) and self.isValidBST(root.right, lt, root.val)
