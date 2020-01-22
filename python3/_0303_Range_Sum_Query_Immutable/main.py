from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.rangeSum = [[0] * n for _ in range(n)]

        self.curSum = [0] * (n + 1)
        for i in range(n):
            self.curSum[i + 1] = self.curSum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.curSum[j + 1] - self.curSum[i]
