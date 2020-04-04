from python3.common.define import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev = cur = dummy
        for i in range(n):
            cur = cur.next

        while cur.next:
            prev = prev.next
            cur = cur.next

        prev.next = prev.next.next
        return dummy.next
