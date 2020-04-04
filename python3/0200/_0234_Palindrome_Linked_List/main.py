from python3.common.define import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        rHead = self.reverse(slow.next)
        slow.next = None

        while head and rHead:
            if head.val != rHead.val:
                return False
            head = head.next
            rHead = rHead.next

        return True

    def reverse(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        while head:
            t = head.next

            head.next = dummy.next
            dummy.next = head

            head = t

        return dummy.next
