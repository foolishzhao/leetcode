from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []

        res = []
        self.dfs(res, "", n, n)
        return res

    def dfs(self, res: List[str], oneRes: str, left: int, right: int):
        if not left and not right:
            res.append(oneRes)
            return
        elif left > right or left < 0:
            return

        self.dfs(res, oneRes + '(', left - 1, right)
        self.dfs(res, oneRes + ')', left, right - 1)
