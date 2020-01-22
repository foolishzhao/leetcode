from python3.common.define import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(0)
        c = 0
        while l1 or l2 or c:
            if l1:
                c += l1.val
                l1 = l1.next

            if l2:
                c += l2.val
                l2 = l2.next

            tail.next = ListNode(c % 10)
            tail = tail.next

            c //= 10

        return dummy.next
