from python3.common.define import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        fast = self.reverseList(fast)
        slow.next = None

        dummy = tail = ListNode(0)
        while head and fast:
            tail.next = head
            tail = tail.next
            head = head.next

            tail.next = fast
            tail = tail.next
            fast = fast.next

        tail.next = head
        return dummy.next

    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        while head:
            t = head.next

            head.next = dummy.next
            dummy.next = head

            head = t

        return dummy.next
