from python3.common.define import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        dummy = ListNode()
        while head:
            t = head.next
            head.next = dummy.next
            dummy.next = head
            head = t
        return dummy.next

    def reverseList2(self,ohead: ListNode,nhead: ListNode) -> ListNode:
        if ohead:
            t = ohead.next
            ohead.next = nhead
            return Solution.reverseList2(t, nhead)
        return nhead

