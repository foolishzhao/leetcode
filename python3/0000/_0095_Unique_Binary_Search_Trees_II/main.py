from python3.common.define import TreeNode
from typing import List
from typing import Optional


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(begin, end):
            if begin > end:
                return [None]

            res = list()
            for i in range(begin, end + 1):
                leftRes = dfs(begin, i - 1)
                rightRes = dfs(i + 1, end)
                for l in leftRes:
                    for r in rightRes:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return dfs(1, n)
