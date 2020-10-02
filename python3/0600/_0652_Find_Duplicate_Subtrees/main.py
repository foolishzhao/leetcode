from python3.common.define import TreeNode
import collections
from typing import List


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def trv(cur):
            if not cur:
                return '#'
            t = str(cur.val) + "," + trv(cur.left) + "," + trv(cur.right)
            if dt[t] == 1:
                res.append(cur)
            dt[t] += 1
            return t

        dt = collections.defaultdict(int)
        res = list()
        trv(root)
        return res
