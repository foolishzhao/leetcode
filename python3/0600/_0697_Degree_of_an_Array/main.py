from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dt = dict()
        for i, num in enumerate(nums):
            if num in dt:
                freq, s, e = dt[num]
                dt[num] = freq + 1, s, i
            else:
                dt[num] = 1, i, i

        maxFreq, res = 0, len(nums)
        for freq, s, e in dt.values():
            if freq > maxFreq:
                maxFreq = freq
                res = e - s + 1
            elif freq == maxFreq:
                res = min(res, e - s + 1)
        return res
