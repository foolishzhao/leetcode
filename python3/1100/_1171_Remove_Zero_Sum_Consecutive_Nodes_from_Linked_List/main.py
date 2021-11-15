from typing import Optional
from python3.common.define import ListNode


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        dt, prefix = {0: dummy}, 0
        nodeToPrefix = {dummy: 0}
        while head:
            prefix += head.val
            if prefix in dt:
                cur = dt[prefix].next
                while cur != head:
                    del dt[nodeToPrefix[cur]]
                    cur = cur.next

                dt[prefix].next = head.next
            else:
                dt[prefix] = head
                nodeToPrefix[head] = prefix
            head = head.next

        return dummy.next

    def removeZeroSumSublists2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        dt, prefix = {0: dummy}, 0
        while head:
            prefix += head.val
            dt[prefix] = head
            head = head.next

        prefix, head = 0, dummy
        while head:
            prefix += head.val
            head.next = dt[prefix].next
            head = head.next

        return dummy.next
