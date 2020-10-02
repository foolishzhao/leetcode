from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        used, n = False, len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if used:
                    return False

                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                elif i + 1 == n - 1 or nums[i + 2] >= nums[i]:
                    nums[i + 1] = nums[i]
                else:
                    return False
                used = True
        return True

    def checkPossibility2(self, nums: List[int]) -> bool:
        used, n = False, len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if used:
                    return False
                used = True

                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
        return True
