from typing import Optional

from python3.common.define import ListNode

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        class Solution:
            def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
                low = head
                fast = head
                while fast and fast.next:
                    low = low.next
                    fast = fast.next.next
                return low





