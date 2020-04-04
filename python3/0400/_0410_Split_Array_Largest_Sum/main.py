from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (right - left) // 2 + left
            if self.isValid(nums, m, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def isValid(self, nums, m, t):
        cnt, curSum = 0, 0
        for num in nums:
            curSum += num
            if curSum > t:
                cnt += 1
                # already m groups, but still has num left
                if cnt >= m:
                    return False

                curSum = num

        return True
