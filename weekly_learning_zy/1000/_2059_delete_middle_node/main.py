# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from python3.common.define import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy.next

    def deleteMiddle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and not head.next: return None
        slow, fast = head, head
        while fast and fast.next:
            tail = slow
            slow = slow.next
            fast = fast.next.next
        tail.next = slow.next
        return head
