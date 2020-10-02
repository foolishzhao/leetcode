from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        # smallest tail of all increasing subsequences with length i+1
        tail = [nums[0]]
        for i in range(1, n):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
            else:
                idx = self.searchGreatEq(tail, nums[i])
                tail[idx] = nums[i]

        return len(tail)

    # tail[idx - 1] < target <= tail[idx]
    def searchGreatEq(self, tail, target):
        left, right = 0, len(tail) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if tail[mid] >= target:
                if mid == left or tail[mid - 1] < target:
                    return mid
                right = mid - 1
            else:
                left = mid + 1

    def lengthOfLIS3(self, nums: List[int]) -> int:
        tail = list()
        for num in nums:
            if not tail or tail[-1] < num:
                tail.append(num)
            else:
                idx = bisect.bisect_left(tail, num)
                tail[idx] = num
        return len(tail)


if __name__ == '__main__':
    Solution().lengthOfLIS2([10, 9, 2, 5, 3, 4])
