from python3.common.define import ListNode

class Solution:
    def deleteDuplicatesii (self, head: ListNode) -> ListNode:
        tail = dummy = ListNode(0)

        while head:
            if head.next and head.val == head.next.val:
                check_val = head.val
                while head and head.val == check_val:
                    head = head.next
            else:
                tail.next = head
                tail = tail.next
                head = head.next
        tail.next = None
        return dummy.next
