from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def dfs(cur, idx):
            nonlocal res
            if idx == m:
                res = min(res, cur, key=lambda x: (abs(x - target), x))
                return

            dfs(cur, idx + 1)
            dfs(cur + toppingCosts[idx], idx + 1)
            dfs(cur + toppingCosts[idx] * 2, idx + 1)

        m, res = len(toppingCosts), float('inf')
        for base in baseCosts:
            dfs(base, 0)
        return res
