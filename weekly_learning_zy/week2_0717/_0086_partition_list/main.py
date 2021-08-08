from python3.common.define import ListNode


class Solution:
    def partitionList(self, head: ListNode, k: int) -> ListNode:
        dummy1, dummy2 = ListNode(0), ListNode(0)
        cur, cur1, cur2 = head, dummy1, dummy2
        if not head or not head.next:
            return head
        while cur:
            if cur.val < k:
                cur1.next = cur
                cur1 = cur1.next
                cur = cur.next
            else:
                cur2.next = cur
                cur2 = cur2.next
                cur = cur.next

        cur1.next = dummy2.next
        cur2.next = None
        return dummy1.next
