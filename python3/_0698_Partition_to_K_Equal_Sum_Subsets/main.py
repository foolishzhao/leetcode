from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k:
            return False

        m, n = s // k, len(nums)
        if max(nums) > m:
            return False

        return self.dfs(nums, [False] * n, k, 0, 0, m)

    def dfs(self, nums, visited, k, curSum, curPos, target):
        if k == 1:
            return True

        if curSum == target:
            return self.dfs(nums, visited, k - 1, 0, 0, target)
        elif curSum > target:
            return False
        else:
            for i in range(curPos, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if self.dfs(nums, visited, k, curSum + nums[i], i + 1, target):
                        return True
                    visited[i] = False
            return False
