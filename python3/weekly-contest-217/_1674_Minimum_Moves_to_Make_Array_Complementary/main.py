from typing import List
import collections


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums) // 2
        line = [0] * (2 * limit + 2)
        dt = collections.defaultdict(int)
        for i in range(n):
            a, b = nums[i], nums[len(nums) - i - 1]
            l, r = min(a, b) + 1, max(a, b) + limit
            line[l] += 1
            line[r + 1] -= 1
            dt[a + b] += 1

        cur, res = 0, float('inf')
        for i, v in enumerate(line):
            cur += v
            mov = cur * 1 + (n - cur) * 2 - dt[i]
            res = min(res, mov)
        return res
