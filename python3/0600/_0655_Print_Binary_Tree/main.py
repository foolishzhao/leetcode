from python3.common.define import TreeNode
from typing import List


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def helper(cur, r, cb, ce):
            if not cur:
                return
            m = (cb + ce) // 2
            res[r][m] = str(cur.val)
            helper(cur.left, r + 1, cb, m - 1)
            helper(cur.right, r + 1, m + 1, ce)

        h = self.getHeight(root)
        n = 2 ** h - 1
        res = [[""] * n for _ in range(h)]
        helper(root, 0, 0, n - 1)
        return res

    def getHeight(self, root):
        return 0 if not root else 1 + max(self.getHeight(root.left), self.getHeight(root.right))
