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
        dummy2 = tail2 = ListNode(1)
        dummy3 = tail3 = ListNode(3)
        tail.next = head
        while left-2 > 0:
            tail = tail.next
            left -= 1
        tail2.next = tail.next
        tail.next = None

        len = 0
        while head:
            head = head.next
            len +=1
        while right-left > 0:
            tail2 = tail2.next
            right -= 1
        if tail2.next:
            tail3.next = tail2.next
            tail2.next = None

        tail.next = reverseList(dummy2.next)

        cur = dummy2
        while cur:
            if cur:
                cur = cur.next
            else:
                cur = tail3.next
        return dummy.next
