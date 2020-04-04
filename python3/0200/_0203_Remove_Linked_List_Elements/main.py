from python3.common.define import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = tail = ListNode(0)
        while head:
            if head.val != val:
                tail.next = head
                tail = tail.next
            head = head.next

        tail.next = None
        return dummy.next
