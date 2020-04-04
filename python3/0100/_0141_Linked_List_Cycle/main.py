from python3.common.define import ListNode


class Solution:
    # time complexity: O(n)
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
