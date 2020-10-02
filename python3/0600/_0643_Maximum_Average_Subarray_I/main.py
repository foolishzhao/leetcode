from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curS = sum(nums[:k])
        res, n = curS / k, len(nums)
        for j in range(k, n):
            curS += nums[j] - nums[j - k]
            res = max(res, curS / k)
        return res
