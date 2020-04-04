from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        nums.sort()
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            for num in nums:
                if i > num:
                    dp[i] += dp[i - num]
                elif i == num:
                    dp[i] += 1
                else:
                    break

        return dp[-1]

    def combinationSum42(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        memo = {0: 1}
        self.dfs(memo, sorted(nums), target)
        return memo[target]

    def dfs(self, memo, nums, target):
        if target in memo:
            return memo[target]

        res = 0
        for num in nums:
            if num <= target:
                res += self.dfs(memo, nums, target - num)
            else:
                break

        memo[target] = res
        return memo[target]
