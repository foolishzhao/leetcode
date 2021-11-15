from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        n = len(nums)
        i, j = n // 2 - 1, len(nums) - 1
        res = list()
        while i >= 0 or j >= n // 2:
            res.append(nums[j])
            j -= 1
            if i >= 0:
                res.append(nums[i])
                i -= 1
        return res

    def rearrangeArray2(self, nums: List[int]) -> List[int]:
        nums.sort()

        for i in range(1, len(nums), 2):
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
        return nums
