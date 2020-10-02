from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            res = str(nums[0]) + "/("
            for num in nums[1:]:
                res += str(num) + '/'
            return res[:-1] + ')'

    def optimalDivision2(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        if len(nums) <= 2:
            return '/'.join(nums)
        else:
            return "{}/({})".format(nums[0], '/'.join(nums[1:]))
