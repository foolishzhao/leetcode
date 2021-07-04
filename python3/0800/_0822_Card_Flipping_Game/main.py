from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad, nums = set(), set()
        for f, b in zip(fronts, backs):
            if f == b:
                bad.add(f)
            nums.add(f)
            nums.add(b)

        nums = sorted(list(nums))
        for num in nums:
            if num not in bad:
                return num
        return 0
