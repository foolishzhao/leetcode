from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return list()

        res = [root.val]
        for c in root.children:
            res.extend(self.preorder(c))
        return res

    def preorder2(self, root: 'Node') -> List[int]:
        res, st = list(), [root]
        while st:
            cur = st.pop()
            if cur:
                res.append(cur.val)
                for c in reversed(cur.children):
                    st.append(c)
        return res
