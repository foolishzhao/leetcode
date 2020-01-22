from python3.common.define import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(-(1 << 31))
        while head:
            t = head.next

            cur = dummy
            while cur.next and cur.next.val <= head.val:
                cur = cur.next

            head.next = cur.next
            cur.next = head

            head = t

        return dummy.next
