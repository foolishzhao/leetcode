from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n, i = len(nums), 0
        while i < n:
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            i += 1

        return [v for i, v in enumerate(nums) if v != i + 1]

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        res = list()
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            nums[abs(num) - 1] *= -1

        return res
