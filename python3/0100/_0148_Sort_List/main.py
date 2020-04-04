from python3.common.define import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        rRes = self.sortList(slow.next)

        slow.next = None
        lRes = self.sortList(head)

        dummy = tail = ListNode(0)
        while lRes and rRes:
            if lRes.val <= rRes.val:
                tail.next = lRes
                tail = tail.next
                lRes = lRes.next
            else:
                tail.next = rRes
                tail = tail.next
                rRes = rRes.next

        if lRes:
            tail.next = lRes
        else:
            tail.next = rRes

        return dummy.next
