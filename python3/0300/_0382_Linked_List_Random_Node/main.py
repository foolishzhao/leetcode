from python3.common.define import ListNode
import random


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res, index, cur = -1, 0, self.head
        while cur:
            if not random.randint(0, index):
                res = cur.val
            index += 1
            cur = cur.next

        return res
