from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        cur, s = 0, sum(nums)
        for i, num in enumerate(nums):
            cur += num
            if cur * 2 > s:
                return nums[:i + 1]
