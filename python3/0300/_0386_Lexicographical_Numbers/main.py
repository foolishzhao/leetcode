from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = list()
        for i in range(1, 10):
            self.dfs(i, n, res)

        return res

    def dfs(self, cur, n, res):
        if cur > n:
            return

        res.append(cur)
        for i in range(10):
            self.dfs(cur * 10 + i, n, res)
