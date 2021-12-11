from python3.common.define import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseList(head):
            dummy = ListNode()
            while head:
                t = head.next
                head.next = dummy.next
                dummy.next = head
                head = t
            return dummy.next

        dummy = tail = ListNode()
        while head:
            prev, cur, cnt = None, head, 0
            while cur and cnt < k:
                prev = cur
                cur = cur.next
                cnt += 1

            if cnt == k:
                prev.next = None
                tail.next = reverseList(head)
                while tail.next:
                    tail = tail.next
                head = cur
            else:
                tail.next = head
                head = None
        return dummy.next

    def reverseKGroup2(self,head:ListNode ,k:int) ->ListNode:

        def reverseList2(head):
            dummy = ListNode()
            while head:
                t = head.next
                head.next = dummy.next
                dummy.next = head
                head = t
            return dummy.next

        dummy = tail = ListNode(0)

        if not head or not head.next or k == 1:
            return head
        while head:
            prev, cur, cnt = None, head, 0
            while cur and cnt< k:
                prev = cur
                cur = cur.next
                cnt += 1
            if cnt == k:
                prev.next = None
                tail.next = reverseList2(head)
                while tail.next:
                    tail = tail.next
                head = cur
            else:
                tail.next = head
                head = None
            return  dummy.next





