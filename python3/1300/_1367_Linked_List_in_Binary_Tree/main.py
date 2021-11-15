from typing import Optional
from python3.common.define import ListNode, TreeNode


class Solution:
    def isStrictSubPath(self, head, root):
        if not head:
            return True

        if not root:
            return False

        if head.val != root.val:
            return False

        return self.isStrictSubPath(head.next, root.left) or self.isStrictSubPath(head.next, root.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True

        if not root:
            return False

        if head.val == root.val and self.isStrictSubPath(head, root):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
