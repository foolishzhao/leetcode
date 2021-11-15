from python3.common.define import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p, n = head, 0
        while p:
            n += 1
            p = p.next

        for _ in range(n // 2):
            head = head.next
        return head
