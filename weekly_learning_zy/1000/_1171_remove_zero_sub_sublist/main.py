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


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        while True:
            dt, prefix = {0: dummy}, 0
            while head:
                prefix += head.val
                if prefix in dt:
                    dt[prefix].next = head.next
                    break
                dt[prefix] = head
                head = head.next

            if head:
                head = dummy.next
            else:
                break
        return dummy.next