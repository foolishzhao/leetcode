from python3.common.define import TreeNode
from typing import Optional


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            nonlocal prev
            if not root:
                return

            dfs(root.left)

            if prev and prev.val > root.val:
                pairs.append([prev, root])
            prev = root

            dfs(root.right)

        pairs, prev = list(), None
        dfs(root)
        pairs[0][0].val, pairs[-1][1].val = pairs[-1][1].val, pairs[0][0].val
