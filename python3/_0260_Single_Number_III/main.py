from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xRes = 0
        for num in nums:
            xRes ^= num

        bit = 1
        while not (xRes & bit):
            bit <<= 1

        first, second = 0, 0
        for num in nums:
            if num & bit:
                first ^= num
            else:
                second ^= num

        return [first, second]
