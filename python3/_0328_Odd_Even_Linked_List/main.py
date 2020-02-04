from python3.common.define import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddDummy = oddTail = ListNode(0)
        evenDummy = evenTail = ListNode(0)
        while head:
            oddTail.next = head
            oddTail = oddTail.next

            head = head.next
            if head:
                evenTail.next = head
                evenTail = evenTail.next
                head = head.next

        oddTail.next = evenDummy.next
        evenTail.next = None
        return oddDummy.next
