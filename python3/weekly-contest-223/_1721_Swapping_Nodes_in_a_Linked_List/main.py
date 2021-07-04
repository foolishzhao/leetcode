from python3.common import ListNode


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        cur, n = head, 0
        while cur:
            cur = cur.next
            n += 1

        fromB, curB = head, k
        while curB > 1:
            fromB = fromB.next
            curB -= 1

        fromE, curE = head, n - k + 1
        while curE > 1:
            fromE = fromE.next
            curE -= 1

        t = fromB.val
        fromB.val = fromE.val
        fromE.val = t

        return head
