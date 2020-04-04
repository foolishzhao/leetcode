from python3.common.define import ListNode
from typing import List
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        dummy = tail = ListNode(0)

        # default min heap, sort by the first elem, then second, then ...
        pq = PriorityQueue()
        for idx, li in enumerate(lists):
            if li:
                pq.put((li.val, idx, li))

        while not pq.empty():
            _, idx, cur = pq.get()

            tail.next = cur
            tail = tail.next

            cur = cur.next

            if cur:
                pq.put((cur.val, idx, cur))

        return dummy.next
