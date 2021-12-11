
from python3.common.define import ListNode

# head -> circle head: x
# circle head -> crossing point: y
# crossing point -> circle head: z
# circle length: y + z
#
# slow, fast: start with same point
#
# slow: x + y + n * (y + z)
# fast: x + y + m * (y + z)
#
#
# 2 * (x + y + n * (y + z)) = x + y + m * (y + z)
#
# x + y = (m - 2n) * (y + z)
#
# x = (m - 2n) * (y + z) - y
# x = (m - 2n - 1) * (y + z) + z
# 如果此时节点A从head出发，节点B从crossing point出发，速度一样， A走过x到达circle head的时候，相当于 b 走过了 (m - 2n - 1) * (y + z) + z ,前一部分
# 相当于在绕圈，后一部分刚好是可以走到circle head， 所以此时AB 是相遇的，相遇的点就是circle head
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head is not slow:
                    head = head.next
                    slow = slow.next

                return head

        return None