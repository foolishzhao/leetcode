from python3.common.define import TreeNode
from typing import List


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        lRes = self.postorderTraversal(root.left)
        rRes = self.postorderTraversal(root.right)
        lRes.extend(rRes)
        lRes.append(root.val)

        return lRes

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        st = [root]
        while st:
            cur = st.pop()
            if cur:
                res.append(cur.val)
                st.append(cur.left)
                st.append(cur.right)

        res.reverse()
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        while root:
            if root.right:
                cur = root.right
                while cur.left and cur.left != root:
                    cur = cur.left

                if not cur.left:
                    res.append(root.val)
                    cur.left = root
                    root = root.right
                else:
                    cur.left = None
                    root = root.left
            else:
                res.append(root.val)
                root = root.left

        res.reverse()
        return res
