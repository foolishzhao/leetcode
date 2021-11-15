from typing import Optional
from python3.common.define import ListNode


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, p = 0, head
        while p:
            n += 1
            p = p.next

        n -= 1
        p, gl = head, 2
        while p and n:
            cl = min(gl, n)
            n -= cl
            if cl % 2 == 1:
                while p and cl:
                    p = p.next
                    cl -= 1
            else:
                q = p.next
                p.next = None
                while q and cl:
                    t = q.next
                    q.next = p.next
                    p.next = q
                    q = t
                    cl -= 1
                while p.next:
                    p = p.next
                p.next = q
            gl += 1

        return head
