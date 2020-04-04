from typing import List
import bisect


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res, n = list(), len(nums)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    cnt += 1
            res.append(cnt)

        return res

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        res = list()
        sortedNums = sorted(nums)
        for num in nums:
            res.append(bisect.bisect_left(sortedNums, num))

        return res
