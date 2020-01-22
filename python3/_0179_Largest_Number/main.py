from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x: str, y: str) -> int:
            if x + y > y + x:
                return -1
            elif x + y == y + x:
                return 0
            else:
                return 1

        if not nums:
            return ""

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(cmp))

        return "".join(nums).lstrip('0') or '0'
