from python3.common.define import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = tail = ListNode(0)
        while head:
            if head.next:
                t = head.next.next

                tail.next = head.next
                tail = tail.next
                tail.next = head
                tail = tail.next

                head = t
            else:
                tail.next = head
                tail = tail.next
                head = None

        tail.next = None
        return dummy.next
