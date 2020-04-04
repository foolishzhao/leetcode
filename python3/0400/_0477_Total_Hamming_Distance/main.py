from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res, bit = 0, 1
        for _ in range(32):
            zeroCount, oneCount = 0, 0
            for num in nums:
                if num & bit:
                    oneCount += 1
                else:
                    zeroCount += 1
            bit <<= 1
            res += oneCount * zeroCount

        return res

    def totalHammingDistance2(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        for i in range(32):
            oneCount = sum([1 for num in nums if ((num >> i) & 1)])
            res += oneCount * (n - oneCount)
        return res

    def totalHammingDistance3(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        for i in range(32):
            oneCount = sum([1 if ((num >> i) & 1) else 0 for num in nums])
            res += oneCount * (n - oneCount)
        return res
