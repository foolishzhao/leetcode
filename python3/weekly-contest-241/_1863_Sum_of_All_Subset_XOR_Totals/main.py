from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n, res = len(nums), 0

        def xorTotal(subset):
            t = 0
            for x in subset:
                t ^= x
            return t

        def dfs(pos, subset):
            if pos == n:
                nonlocal res
                res += xorTotal(subset)
                return

            dfs(pos + 1, subset)
            subset.append(nums[pos])
            dfs(pos + 1, subset)
            subset.pop()

        dfs(0, list())
        return res

    def subsetXORSum2(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        for i in range(1, 1 << n):
            curRes = 0
            for j in range(0, n):
                if i & (1 << j):
                    curRes ^= nums[j]
            res += curRes
        return res
