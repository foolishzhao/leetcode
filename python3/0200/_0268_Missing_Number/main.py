from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i, n = 0, len(nums)
        while i < n:
            num = nums[i]
            while num != i and num < n and num != nums[num]:
                nums[i], nums[num] = nums[num], num
                # remember to update num
                num = nums[i]
            i += 1

        for i, num in enumerate(nums):
            if num != i:
                return i

        return n

    def missingNumber2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i, n = 0, len(nums)
        while i < n:
            if nums[i] != i and nums[i] < n and nums[i] != nums[nums[i]]:
                # need to use t
                t = nums[i]
                nums[i], nums[t] = nums[t], nums[i]
            else:
                i += 1

        for i, num in enumerate(nums):
            if num != i:
                return i

        return n

    def missingNumber3(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
