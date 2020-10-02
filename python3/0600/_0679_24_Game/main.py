from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.dfs(nums)

    def dfs(self, nums):
        n = len(nums)
        if n == 1:
            return abs(nums[0] - 24) < 1e-5

        for i, u in enumerate(nums):
            for j, v in enumerate(nums[:i]):
                nxt = [u + v, u - v, v - u, u * v]
                if abs(u) > 1e-5:
                    nxt.append(v / u)
                if abs(v) > 1e-5:
                    nxt.append(u / v)

                sub = [nums[x] for x in range(n) if (x != i and x != j)]
                for k in nxt:
                    if self.dfs(sub + [k]):
                        return True
        return False
