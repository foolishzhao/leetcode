from python3.common.define import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = tail = ListNode(None)
        while head:
            if head.val != val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return dummy.next
