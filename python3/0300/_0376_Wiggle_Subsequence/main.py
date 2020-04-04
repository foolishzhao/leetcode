from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        up, down = [0] * n, [0] * n
        up[0] = down[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = up[i - 1] + 1
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[-1], down[-1])

    # save space
    def wiggleMaxLength2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n, up, down = len(nums), 1, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)
