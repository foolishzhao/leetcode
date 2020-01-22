from python3.common.define import Node


class Solution:
    # iterate
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            dummy = tail = Node()
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next

                if cur.right:
                    tail.next = cur.right
                    tail = tail.next

                cur = cur.next

            cur = dummy.next

        return root

    # recursive
    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return root

        dummy = tail = Node()
        cur = root
        while cur:
            if cur.left:
                tail.next = cur.left
                tail = tail.next

            if cur.right:
                tail.next = cur.right
                tail = tail.next

            cur = cur.next

        self.connect(dummy.next)

        return root
