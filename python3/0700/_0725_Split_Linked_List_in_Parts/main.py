from python3.common.define import ListNode
from typing import List


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n, cur = 0, root
        while cur:
            n += 1
            cur = cur.next

        res, cur, avg, ext = list(), root, n // k, n % k
        for _ in range(k):
            dummy = ListNode(0)
            tail = dummy
            for _ in range(avg + (ext > 0)):
                tail.next = cur
                tail = tail.next
                cur = cur.next
            ext -= 1
            tail.next = None
            res.append(dummy.next)
        return res
