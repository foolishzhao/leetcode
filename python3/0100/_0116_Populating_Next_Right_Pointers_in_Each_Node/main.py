from python3.common.define import Node
from queue import Queue


class Solution:
    # bfs
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        q = Queue()
        q.put(root)

        while not q.empty():
            cur = q.get()
            if cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left

                q.put(cur.left)
                q.put(cur.right)

        return root

    # dfs
    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return root

        st = [root]
        while st:
            cur = st.pop()
            if cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left

                st.append(cur.right)
                st.append(cur.left)

        return root

    # iterate
    def connect3(self, root: 'Node') -> 'Node':
        cur, nxt = root, None
        while cur and cur.left:
            nxt = cur.left
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left

                cur = cur.next

            cur = nxt

        return root

    # recursive
    def connect4(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
