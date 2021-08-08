from python3.common.define import ListNode


class Solution:
    def rotateList(self, head: ListNode, k: int) -> ListNode:

        dummy = tail = ListNode(0)
        if not head or not head.next or k == 0:
            return head
        len = 0
        cur = head
        while cur:
            len += 1
            cur = cur.next
        k = k % len
        if k == 0:
            return head
        cur = head
        while k > 0:
            k -= 1
            cur = cur.next
        tail = head
        while cur.next:
            tail = tail.next
            cur = cur.next
        dummy.next = tail.next
        cur.next = head
        tail.next = None

        return dummy.next

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        p, n = head, 1
        while p.next:
            n += 1
            p = p.next

        k %= n
        if not k:
            return head

        q = head
        while n - k > 1:
            q = q.next
            k += 1

        res = q.next
        q.next = None
        p.next = head
        return res
