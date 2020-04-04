from typing import List
import collections
import functools


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [collections.defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i, v in enumerate(nums):
            for t, cnt in dp[i].items():
                dp[i + 1][t + v] += cnt
                dp[i + 1][t - v] += cnt

        return dp[-1][S]

    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        dt = collections.defaultdict(int)
        dt[0] = 1
        for i, v in enumerate(nums):
            nxtDt = collections.defaultdict(int)
            for curSum, cnt in dt.items():
                nxtDt[curSum + v] += cnt
                nxtDt[curSum - v] += cnt
            dt = nxtDt
        return dt[S]


class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @functools.lru_cache(None)
        def dfs(pos, curSum):
            if pos == len(nums):
                return 1 if curSum == S else 0
            return dfs(pos + 1, curSum + nums[pos]) + dfs(pos + 1, curSum - nums[pos])

        return dfs(0, 0)
