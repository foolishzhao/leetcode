from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1

        dt = {0: -1}
        res, cur = 0, 0
        for i, num in enumerate(nums):
            cur += num
            if cur in dt:
                res = max(res, i - dt[cur])
            else:
                dt[cur] = i
        return res
