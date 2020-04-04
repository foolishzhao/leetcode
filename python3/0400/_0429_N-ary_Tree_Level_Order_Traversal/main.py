from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = list()
        if not root:
            return res

        q = [root]
        while q:
            curRes = list()

            sz = len(q)
            for _ in range(sz):
                cur = q.pop(0)
                curRes.append(cur.val)
                for c in cur.children:
                    q.append(c)

            res.append(curRes)

        return res
