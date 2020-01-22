from typing import List
from python3.common.define import TreeNode
from queue import Queue


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = Queue()
        q.put(root)

        res = []
        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                cur = q.get()
                if i == sz - 1:
                    res.append(cur.val)
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)

        return res

    def rightSideView2(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        self.dfs(res, root, 0)
        return res

    def dfs(self, res: List[int], root: TreeNode, depth: int) -> None:
        if root:
            if len(res) == depth:
                res.append(root.val)

            self.dfs(res, root.right, depth + 1)
            self.dfs(res, root.left, depth + 1)
