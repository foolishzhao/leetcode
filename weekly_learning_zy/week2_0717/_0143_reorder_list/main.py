from python3.common.define import ListNode

class Solution:
    def reorderList(self, head:ListNode) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, slow.next, slow = None, None, slow.next

        while slow:
            prev, prev.next, slow = slow, prev, slow.next

        slow = head
        while prev:
            slow.next, slow = prev, slow.next
            prev.next, prev = slow, prev.next

    def reorderListbyzy(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dummy, slow.next, slow = ListNode(0), None, slow.next
        while slow:
            tmp = slow.next
            slow.next = dummy.next
            dummy.next = slow
            slow = tmp

            # prev, prev.next, slow = slow, prev, slow.next

        slow = head
        while dummy.next:
            slow.next, slow = dummy.next, slow.next
            dummy.next.next, dummy.next = slow, dummy.next.next

    def reorderList2(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        if fast.next:
            fast = fast.next

        # reverse the second half of the list
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp



        # turn the list into zigzag manner
        trav = head
        while fast.next:
            tmp1 = trav.next
            tmp2 = fast.next
            trav.next = fast
            fast.next = tmp1
            trav = tmp1
            fast = tmp2