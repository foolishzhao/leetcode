from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(res, [], 1, k, n)
        return res

    def dfs(self, res, curRes, curNum, k, n):
        if len(curRes) == k:
            if n == 0:
                res.append(curRes)
            return
        elif n < 0 or curNum > 9:
            return

        self.dfs(res, curRes, curNum + 1, k, n)
        self.dfs(res, curRes + [curNum], curNum + 1, k, n - curNum)
