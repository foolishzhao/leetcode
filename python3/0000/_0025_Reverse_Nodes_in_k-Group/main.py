from python3.common.define import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k <= 1:
            return head

        dummy = tail = ListNode(0)
        while head:
            cnt = 1
            cur = head
            while cur and cnt < k:
                cnt += 1
                cur = cur.next

            if cur:
                t = cur.next

                cur.next = None
                while head:
                    tt = head.next
                    head.next = tail.next
                    tail.next = head
                    head = tt

                while tail.next:
                    tail = tail.next

                head = t
            else:
                tail.next = head
                head = None

        return dummy.next
