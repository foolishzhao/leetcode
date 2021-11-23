from python3.common.define import ListNode


class Solution:
    def add_to_sorted_list(self, head, dummy, tail):
        if dummy == tail or head.val >= tail.val:
            tail.next = head
            head.next = None
            tail = head
        else:
            while dummy.next and dummy.next.val <= head.val:
                dummy = dummy.next
            head.next = dummy.next
            dummy.next = head
        return tail

    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = tail = ListNode(None)
        while head:
            tmp = head.next
            tail = self.add_to_sorted_list(head, dummy, tail)
            head = tmp
        return dummy.next
