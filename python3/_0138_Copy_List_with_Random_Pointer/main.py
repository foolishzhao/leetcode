class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        dt = dict()
        cur = head
        while cur:
            dt[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                dt[cur].next = dt[cur.next]
            if cur.random:
                dt[cur].random = dt[cur.random]

            cur = cur.next

        return dt[head]

    def copyRandomList2(self, head: 'Node') -> 'Node':
        if not head:
            return None

        cur = head
        while cur:
            cpy = Node(cur.val, None, None)
            cpy.next = cur.next
            cur.next = cpy

            cur = cpy.next

        # note that random can point to before node, so need to set random before separate
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # need to restore origin link list
        dummy = tail = Node(0, None, None)
        while head:
            tail.next = head.next
            tail = tail.next

            head.next = tail.next
            head = head.next

        return dummy.next
