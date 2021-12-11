from typing import Optional

from python3.common.define import ListNode


class Solution:
    def reservelist(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)

        while head:
            t = head.next
            head.next = dummy.next
            dummy.next = head
            head = t
        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1s = self.reservelist(l1)
        l2s = self.reservelist(l2)
        dummy = tail = ListNode(None)
        carry = 0
        while l1s or l2s or carry:
            x = l1s.val if l1s else 0
            y = l2s.val if l2s else 0
            tail.next = ListNode((x + y + carry)%10)
            carry = (x + y + carry) // 10
            tail = tail.next
            if l1s:
                l1s = l1s.next
            if l2s:
                l2s = l2s.next
        dummy.next = self.reservelist(dummy.next)
        return dummy.next


if __name__ == '__main__':
    l1 = [ListNode(x) for x in list(range(1, 6))]
    for i, node in enumerate(l1[:-1]):
        node.next = l1[i + 1]
    l2 = [ListNode(y) for y in list(range(2, 5))]
    for i, node in enumerate(l2[:-1]):
        node.next = l2[i + 1]
    l3 = Solution().addTwoNumbers(l1[0], l2[0])
    while l3:
        print(l3.val)
        l3 = l3.next
