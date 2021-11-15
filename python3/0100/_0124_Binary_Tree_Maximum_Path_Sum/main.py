from python3.common.define import TreeNode
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(cur):
            if not cur:
                return float('-inf'), float('-inf')

            lRes, lMax = dfs(cur.left)
            rRes, rMax = dfs(cur.right)
            return max(lRes, rRes, cur.val + max(lMax, 0) + max(rMax, 0)), cur.val + max(lMax, rMax, 0)

        if not root:
            return 0

        res, _ = dfs(root)
        return res
