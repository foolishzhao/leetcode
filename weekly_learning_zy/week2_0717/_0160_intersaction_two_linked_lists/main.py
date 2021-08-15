from python3.common.define import ListNode

class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        m, n = 0, 0

        p = headA
        while p:
            m += 1
            p = p.next

        p = headB
        while p:
            n += 1
            p = p.next

        while m > n:
            headA = headA.next
            m -= 1

        while m < n:
            headB = headB.next
            n -= 1
        while headA and headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
