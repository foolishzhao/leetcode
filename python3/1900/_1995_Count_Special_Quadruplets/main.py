from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        res += nums[a] + nums[b] + nums[c] == nums[d]
        return res
