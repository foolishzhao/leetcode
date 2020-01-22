from python3.common.define import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        lenA, lenB = self.getLen(headA), self.getLen(headB)
        while lenA > lenB:
            headA = headA.next
            lenA -= 1

        while lenA < lenB:
            headB = headB.next
            lenB -= 1

        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def getLen(self, head: ListNode) -> int:
        res = 0
        while head:
            res += 1
            head = head.next

        return res
