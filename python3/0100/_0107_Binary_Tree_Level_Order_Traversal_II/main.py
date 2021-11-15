from typing import Optional, List
from python3.common.define import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, res = [root], list()
        while q:
            subRes, nq = list(), list()
            for x in q:
                if x:
                    subRes.append(x.val)
                    nq.append(x.left)
                    nq.append(x.right)
            q = nq
            if subRes:
                res.append(subRes)
        return res[::-1]
