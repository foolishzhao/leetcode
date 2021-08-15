from python3.common.define import ListNode


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverseList(head):
            dummy = ListNode()
            while head:
                t = head.next
                head.next = dummy.next
                dummy.next = head
                head = t
            return dummy.next

        if not head or not head.next or left == right:
            return head

        dummy = tail = ListNode(0)
        dummy2 = tail2 = ListNode(501)
        dummy3 = tail3 = ListNode(502)
        tail.next = head

        while left - 1 > 0:
            tail = tail.next
            left -= 1
        tail2.next = tail.next
        tail2 = tail2.next
        tail.next = None

        while right - left > 0:
            tail2 = tail2.next
            right -= 1
        if tail2.next:
            tail3.next = tail2.next
            tail2.next = None

        tail.next = reverseList(dummy2.next)

        cur = dummy2
        while cur.next:
            cur = cur.next
        cur.next = tail3.next
        return dummy.next

    def reverseBetweenHaoran(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse(oldHead, newHead):
            if oldHead:
                t = oldHead.next
                oldHead.next = newHead
                return reverse(t, oldHead)
            return newHead

        dummy = ListNode()
        dummy.next = head

        p, pos = dummy, 0
        while pos < left - 1:
            p = p.next
            pos += 1

        q = p
        while pos < right:
            q = q.next
            pos += 1

        t = q.next
        q.next = None

        p.next = reverse(p.next, None)
        while p.next:
            p = p.next
        p.next = t

        return dummy.next


