from python3.common.define import TreeNode
from typing import Optional
from typing import List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(cur, target, curRes):
            if not cur:
                return

            curRes.append(cur.val)

            target -= cur.val
            if not cur.left and not cur.right:
                if not target:
                    res.append(curRes[:])
            else:
                dfs(cur.left, target, curRes)
                dfs(cur.right, target, curRes)

            curRes.pop()

        res = list()
        dfs(root, targetSum, list())
        return res
