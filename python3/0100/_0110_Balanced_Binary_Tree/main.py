from python3.common.define import TreeNode
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur):
            if not cur:
                return True, 0

            lb, lh = dfs(cur.left)
            rb, rh = dfs(cur.right)
            if not lb or not rb or abs(lh - rh) > 1:
                return False, 0

            return True, 1 + max(lh, rh)

        b, _ = dfs(root)
        return b
