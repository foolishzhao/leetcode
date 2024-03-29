from typing import Optional, List

from python3.common.define import ListNode


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        list = []
        if not head or not head.next:
            list.append(0)
            return list
        while head:
            cur = head
            while cur and cur.next:
                if cur.next.val > head.val:
                    list.append(cur.next.val)
                    break
                else:
                    cur = cur.next
            if cur == None or cur.next == None:
                list.append(0)

            head = head.next
        return list

    def nextLargerNodes(self, head):
        res, stack = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append([len(res), head.val])
            res.append(0)
            head = head.next
        return res



