from python3.common.define import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge(a, b):

            if not a:
                return b

            elif not b:
                return a

            if a.val < b.val:
                a.next = merge(a.next, b)
                return a

            else:
                b.next = merge(a, b.next)
                return b

        # -------------------------------

        ## base case
        if not head or not head.next:
            return head

        ## general case
        # divide into two halves

        pre, slow, fast = None, head, head

        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None

        # sort by divide-and-conquer

        first_half = self.sortList(head)
        second_half = self.sortList(slow)
        result = merge(first_half, second_half)
        return result
