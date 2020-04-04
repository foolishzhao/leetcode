from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        one, two = 0, 0
        for _, v in enumerate(nums):
            two |= (one & v)
            one ^= v

            three = one & two
            one &= ~three
            two &= ~three

        return one
