class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        dummy = Node(0, None, None, None)
        tail = dummy

        st = [head]
        while st:
            cur = st.pop()
            while cur:
                tail.next = cur
                cur.prev = tail

                if cur.child:
                    st.append(cur.next)
                    cur = cur.child
                else:
                    cur = cur.next

                tail.child = None
                tail = tail.next

        tail.next = None
        head = dummy.next
        head.prev = None
        return head
