class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class SearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val: int):
        if not self.root:
            self.root = TreeNode(val)
            return

        self._insert(self.root, val)

    def _insert(self, root: TreeNode, val: int):
        if val == root.val:
            return
        elif val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self._insert(root.left, val)
        else:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self._insert(root.right, val)

    def search(self, val: int) -> bool:
        cur = self.root
        while cur:
            if val == cur.val:
                return True
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        return False

    def delete(self, val: int):
        cur, curP = self.root, None
        while cur:
            if val == cur.val:
                break
            elif val < cur.val:
                curP = cur
                cur = cur.left
            else:
                curP = cur
                cur = cur.right

        if not cur:
            return

        if cur.left and cur.right:
            nxt, nxtP = cur.right, cur
            while nxt.left:
                nxtP = nxt
                nxt = nxt.left

            cur.val = nxt.val
            cur, curP = nxt, nxtP

        child = cur.left if cur.left else cur.right

        if not curP:
            self.root = child
        elif curP.left == cur:
            curP.left = child
        else:
            curP.right = child


if __name__ == '__main__':
    st = SearchTree()
    print(st.search(1))
    st.insert(1)
    st.insert(2)
    st.insert(3)
    print(st.search(1))
    print(st.search(4))
    st.delete(1)
    print(st.search(1))
