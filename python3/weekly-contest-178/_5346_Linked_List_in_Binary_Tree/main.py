from python3.common.define import ListNode
from python3.common.define import TreeNode


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False

        if self.checkPath(head, root):
            return True

        if self.isSubPath(head, root.left) or self.isSubPath(head, root.right):
            return True

        return False

    def checkPath(self, head, root):
        if not head:
            return True

        if not root or root.val != head.val:
            return False

        if self.checkPath(head.next, root.left) or self.checkPath(head.next, root.right):
            return True

        return False
