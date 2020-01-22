from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dt = dict()
        for i, num in enumerate(nums):
            if num in dt and i - dt[num] <= k:
                return True
            dt[num] = i

        return False
