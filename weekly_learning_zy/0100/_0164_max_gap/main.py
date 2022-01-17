from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ans = 0
        if not nums or len(nums)==1:
            return ans
        nums.sort()
        for i in range(len(nums)-1):
            ans = max(ans, abs(nums[i+1] - nums[i]) )
        return ans