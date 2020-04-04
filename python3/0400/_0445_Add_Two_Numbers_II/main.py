from python3.common.define import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        st1, st2 = list(), list()
        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next

        tail, c = None, 0
        while st1 or st2 or c:
            cur = c
            if st1:
                cur += st1.pop()

            if st2:
                cur += st2.pop()

            c = cur // 10
            curNode = ListNode(cur % 10)
            curNode.next = tail
            tail = curNode

        return tail
