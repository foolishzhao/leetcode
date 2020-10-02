from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return list()

        res = list()
        for c in root.children:
            res.extend(self.postorder(c))
        res.append(root.val)

        return res

    def postorder2(self, root: 'Node') -> List[int]:
        res, st = list(), [root]
        while st:
            cur = st.pop()
            if cur:
                res.append(cur.val)
                for c in cur.children:
                    st.append(c)
        return res[::-1]
