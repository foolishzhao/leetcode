from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 4:
            return False

        s = sum(nums)
        if s % 4 != 0:
            return False

        edge = s // 4
        if max(nums) > edge:
            return False

        return self.dfs(nums, [False] * len(nums), 4, 0, edge, 0)

    def dfs(self, nums, visited, k, curSum, target, curPos):
        if k == 1:
            return True

        if curSum == target:
            return self.dfs(nums, visited, k - 1, 0, target, 0)
        elif curSum > target:
            return False
        else:
            for i in range(curPos, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if self.dfs(nums, visited, k, curSum + nums[i], target, i + 1):
                        return True
                    visited[i] = False
            return False
