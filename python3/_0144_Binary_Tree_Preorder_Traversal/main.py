from python3.common.define import TreeNode
from typing import List


class Solution:
    # recursive
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = [root.val]
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))

        return res

    # iterate, stack
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        st = [root]
        while st:
            cur = st.pop()
            if cur:
                res.append(cur.val)
                st.append(cur.right)
                st.append(cur.left)

        return res

    # iterate, morris travel
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right

                if not cur.right:
                    res.append(root.val)
                    cur.right = root
                    root = root.left
                else:
                    cur.right = None
                    root = root.right
            else:
                res.append(root.val)
                root = root.right

        return res
