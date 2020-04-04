from typing import List
from python3.common.define import TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res, q = list(), [root]
        while q:
            sz, maxVal = len(q), float('-inf')
            for _ in range(sz):
                cur = q.pop(0)
                if not cur:
                    continue
                maxVal = max(maxVal, cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if maxVal != float('-inf'):
                res.append(maxVal)
        return res

    def largestValues2(self, root: TreeNode) -> List[int]:
        res = list()
        self.dfs(res, root, 0)
        return res

    def dfs(self, res, root, d):
        if not root:
            return

        if d == len(res):
            res.append(root.val)
        else:
            res[d] = max(res[d], root.val)

        self.dfs(res, root.left, d + 1)
        self.dfs(res, root.right, d + 1)
