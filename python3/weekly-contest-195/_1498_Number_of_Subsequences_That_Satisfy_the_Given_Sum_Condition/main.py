from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        i, j, res = 0, len(nums) - 1, 0
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                # min: nums[i], for other j - i nums, exist or not exist
                res += 1 << (j - i)
                i += 1

        return res % (10 ** 9 + 7)
