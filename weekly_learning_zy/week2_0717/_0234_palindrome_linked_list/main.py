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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        p = head
        if not head:
            return false
        while p:
            n = n + 1
            p = p.next
        if n == 2:
            return true
        if n % 2 != 0:
            pre = (n // 2) + 1
        else:
            pre = n // 2
        dummy = tail = ListNode(None)
        tail.next = head
        while pre > 1:
            tail = tail.next
            pre -= 1

        dummy2 = tail2 = ListNode(None)
        tail2.next = tail
        tail.next = None
        while tail2:
            tail2 = tail2.next
        rlink = self.reverseList(dummy2.next)

        while dummy2.next and dummy2.next == dummy.next:
            dummy = dummy.next
            dummy2 = dummy2.next
        if dummy2.next == None:
            return true








