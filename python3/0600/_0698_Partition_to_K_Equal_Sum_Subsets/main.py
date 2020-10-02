from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k:
            return False

        target = sum(nums) // k
        if max(nums) > target:
            return False

        def dfs(curPos, curSum, t):
            if t == 1:
                return True

            for i in range(curPos, n):
                if not visited[i]:
                    visited[i] = True
                    if curSum + nums[i] < target:
                        if dfs(i + 1, curSum + nums[i], t):
                            return True
                    elif curSum + nums[i] == target:
                        if dfs(0, 0, t - 1):
                            return True
                    visited[i] = False
            return False

        n = len(nums)
        visited = [False] * n
        return dfs(0, 0, k)

    # Time complexity: O(n*2^n)
    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k:
            return False

        tar, n = sum(nums) // k, len(nums)
        if max(nums) > tar:
            return False

        dp = [-1] * (1 << n)
        dp[0] = 0
        for i in range(1 << n):
            if dp[i] == -1:
                continue
            for j in range(n):
                if not (i & (1 << j)) and dp[i] + nums[j] <= tar:
                    dp[i | (1 << j)] = (dp[i] + nums[j]) % tar
        return not dp[-1]