from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        while a and b % a:
            b = b % a
            a, b = b, a
        return a
