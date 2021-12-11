from python3.common.define import ListNode
import math

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        len = 0
        res = 0
        p = head
        while p:
            len += 1
            p = p.next
        while head:
            if head.val == 0:
                head = head.next
                res += 0
                len -= 1
            else:
                res = res + math.pow(2,len-1)
                len -= 1
                head = head.next
        return res

    def getDecimalValue2(self, head: ListNode) -> int:
        answer = 0
        while head:
            answer = 2 * answer + head.val
            head = head.next
        return answer
