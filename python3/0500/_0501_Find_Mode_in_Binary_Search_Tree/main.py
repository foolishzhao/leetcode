from typing import List
from python3.common.define import TreeNode


class Solution:
    def __init__(self):
        self.prev = float('-inf')
        self.prevCnt = 0
        self.maxCnt = 0
        self.second = False
        self.res = list()

    def findMode(self, root: TreeNode) -> List[int]:
        self.inOrder(root)
        self.prev = float('-inf')
        self.second = True
        self.inOrder(root)
        return self.res

    def handleVal(self, val):
        if val > self.prev:
            self.prev = val
            self.prevCnt = 1
        else:
            self.prevCnt += 1

        self.maxCnt = max(self.maxCnt, self.prevCnt)
        if self.second and self.prevCnt == self.maxCnt:
            self.res.append(val)

    def inOrder(self, root):
        while root:
            if not root.left:
                self.handleVal(root.val)
                root = root.right
            else:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right

                if cur.right:
                    cur.right = None
                    self.handleVal(root.val)
                    root = root.right
                else:
                    cur.right = root
                    root = root.left
