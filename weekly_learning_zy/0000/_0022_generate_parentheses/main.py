from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(curres, left, right):
            if not left and not right:
                res.append(curres)
                return res
            elif left > right or left < 0:
                return
            dfs(curres+'(',left - 1, right)
            dfs(curres+')',left, right-1)
        if not n:
            return []
        res = []
        dfs("", n, n)
        return res