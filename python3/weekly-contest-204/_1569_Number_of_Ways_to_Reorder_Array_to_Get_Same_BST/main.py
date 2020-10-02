from typing import List
import math


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def dfs(li):
            if len(li) <= 2:
                return 1

            left = [v for v in li if v < li[0]]
            right = [v for v in li if v > li[0]]
            return math.comb(len(left) + len(right), len(left)) * dfs(left) * dfs(right)

        return (dfs(nums) - 1) % (10 ** 9 + 7)
