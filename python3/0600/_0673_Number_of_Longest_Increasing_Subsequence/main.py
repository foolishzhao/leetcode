from typing import List
import functools


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        @functools.lru_cache(None)
        def dp(i, j):
            if j == 1:
                return 1

            if i < j - 1:
                return 0

            res = 0
            for k in range(i):
                if nums[k] < nums[i]:
                    res += dp(k, j - 1)
            return res

        n, m = len(nums), self.getLenOfLIS(nums)
        return sum([dp(i, m) for i in range(n)])

    def getLenOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def findNumberOfLIS2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        length, cnt = [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j] + 1:
                        cnt[i] += cnt[j]
                    elif length[i] < length[j] + 1:
                        length[i] = length[j] + 1
                        cnt[i] = cnt[j]
        maxLen = max(length)
        return sum([x for i, x in enumerate(cnt) if length[i] == maxLen])
