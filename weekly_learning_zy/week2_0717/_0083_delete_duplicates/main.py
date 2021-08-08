from python3.common.define import ListNode


class Solution:
    def deleteduplicates(head: ListNode) -> ListNode:
        dummy = tail = ListNode(0)
        while head:
            if head.next and head.next.val == head.val:
                head = head.next
            else:
                tail.next = head
                tail = tail.next
                head = head.next
        tail.next = head
        return dummy.next

    def deleteduplicates2(self, head: ListNode) -> ListNode:
        dummy = tail = ListNode(0)
        while head:
            if head.val != tail.val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return dummy.next




