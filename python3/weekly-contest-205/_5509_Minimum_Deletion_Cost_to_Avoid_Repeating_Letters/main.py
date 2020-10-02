from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s += 'A'
        cost.append(0)

        n, i, res = len(cost), 0, 0
        for j in range(1, n):
            if s[j] != s[j - 1]:
                if j - 1 > i:
                    res += sum(cost[i: j]) - max(cost[i: j])
                i = j
        return res
