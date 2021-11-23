from typing import Optional

from python3.common.define import ListNode
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even:
            if even.next:
                odd.next = odd.next.next
                even.next = even.next.next
                odd = odd.next
                even = even.next
            else:
                even = even.next
        odd.next = evenHead
        return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy1 = tail1 = ListNode(None)
        dummy2 = tail2 = ListNode(None)
        tail1.next = head
        tail1 = tail1.next

        while head and head.next:
            tail2.next = head.next
            tail2 = tail2.next
            head = head.next

            if head.next:
                tail1.next = head.next
                tail1 = tail1.next
                head = head.next

        tail1.next = dummy2.next

        tail2.next = None
        return dummy1.next

    def oddEvenListhr(self, head: ListNode) -> ListNode:
        dummy1 = tail1 = ListNode()
        dummy2 = tail2 = ListNode()

        while head:
            tail1.next = head
            tail1 = tail1.next
            head = head.next

            if head:
                tail2.next = head
                tail2 = tail2.next
                head = head.next

        tail1.next = dummy2.next
        tail2.next = None
        return dummy1.next