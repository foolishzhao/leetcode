from python3.common.define import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        while head:
            t = head.next
            head.next = dummy.next
            dummy.next = head
            head = t

        return dummy.next

    def reverseList2(self, head: ListNode) -> ListNode:
        return self.reverseListHelper(head, None)

    def reverseListHelper(self, oldHead: ListNode, newHead: ListNode) -> ListNode:
        if oldHead:
            oldNext = oldHead.next
            oldHead.next = newHead
            return self.reverseListHelper(oldNext, oldHead)

        return newHead
