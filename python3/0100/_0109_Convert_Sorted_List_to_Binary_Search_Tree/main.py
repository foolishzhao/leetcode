from python3.common.define import TreeNode
from python3.common.define import ListNode
from typing import Optional


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        prev, slow, fast = None, head, head
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)
        if prev:
            prev.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
