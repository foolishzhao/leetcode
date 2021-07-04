from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n, res = len(nums), nums[k]
        left, right, curMin = k - 1, k + 1, nums[k]
        while left >= 0 or right < n:
            if left < 0 or (right < n and nums[left] <= nums[right]):
                curMin = min(curMin, nums[right])
                right += 1
            else:
                curMin = min(curMin, nums[left])
                left -= 1
            res = max(res, curMin * (right - left - 1))
        return res
