from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        evenLeft, oddLeft, evenRight, oddRight = 0, 0, sum(nums[::2]), sum(nums[1::2])
        res = 0
        for i, v in enumerate(nums):
            if i % 2 == 0:
                evenRight -= v
                res += evenLeft + oddRight == oddLeft + evenRight
                evenLeft += v
            else:
                oddRight -= v
                res += evenLeft + oddRight == oddLeft + evenRight
                oddLeft += v
        return res
