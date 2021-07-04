from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        prev, first = 0, False
        for num in nums:
            if num >= prev:
                prev = num
            else:
                if first:
                    return False
                first = True
                prev = 0

        return not first or nums[0] >= nums[-1]

    def check2(self, nums: List[int]) -> bool:
        return sum(a > b for a, b in zip(nums, nums[1:] + nums[:1])) <= 1

    def check3(self, nums: List[int]) -> bool:
        k = sum(a > b for a, b in zip(nums[:-1], nums[1:]))
        if not k:
            return True
        if k == 1:
            return nums[0] >= nums[-1]
        return False
