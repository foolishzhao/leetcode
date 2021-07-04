from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res, n, cur, i, dt = 0, len(nums), 0, 0, dict()
        for j, num in enumerate(nums):
            if num in dt and dt[num] >= i:
                res = max(res, cur)
                while i <= dt[num]:
                    cur -= nums[i]
                    i += 1
            cur += num
            dt[num] = j
        return max(res, cur)
