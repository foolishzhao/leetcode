from python3.common.define import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        while root:
            self.st.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.st.pop()
        cur = node.right
        while cur:
            self.st.append(cur)
            cur = cur.left

        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.st
