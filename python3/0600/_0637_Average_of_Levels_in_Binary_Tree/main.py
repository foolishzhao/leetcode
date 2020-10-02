from python3.common.define import TreeNode
from typing import List


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = list()
        q = [root]
        while q:
            l, s, c = len(q), 0, 0
            for _ in range(l):
                cur = q.pop(0)
                if cur:
                    s += cur.val
                    c += 1
                    q.append(cur.left)
                    q.append(cur.right)
            if c:
                res.append(s / c)
        return res
