from typing import List, Optional
from python3.common.define import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, res, lv = [root], list(), 0
        while q:
            subRes, nq = list(), list()
            for x in q:
                if x:
                    subRes.append(x.val)
                    nq.append(x.left)
                    nq.append(x.right)
            q = nq
            lv += 1
            if subRes:
                res.append(subRes if lv % 2 == 1 else subRes[::-1])
        return res
