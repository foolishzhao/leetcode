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

    def connect3(self, root: 'Node') -> 'Node':
        if root:
            cur = None
            if root.left and root.right:
                root.left.next = root.right
                cur = root.right
            elif root.left:
                cur = root.left
            elif root.right:
                cur = root.right

            if cur:
                t = root.next
                while t:
                    if t.left or t.right:
                        break
                    t = t.next

                if t:
                    cur.next = t.left if t.left else t.right

            self.connect3(root.right)
            self.connect3(root.left)
        return root


# [2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]
if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)

    root.left.left = Node(0)
    root.left.right = Node(7)

    root.right.left = Node(9)
    root.right.right = Node(1)

    root.left.left.left = Node(2)

    root.left.right.left = Node(1)
    root.left.right.right = Node(0)

    root.right.right.left = Node(8)
    root.right.right.right = Node(8)

    root.left.right.right.left = Node(7)

    Solution().connect3(root)
