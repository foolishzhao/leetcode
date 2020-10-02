from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(i):
            if not visited[i]:
                visited[i] = True
                dp[i] = 1 + dfs(nums[i])
            return dp[i]

        n = len(nums)
        dp = [0] * n
        visited = [False] * n
        return max([dfs(i) for i in range(n)])

    # since elements are distinct, for each group, it's end must connects to it' start.
    def arrayNesting2(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        visited = [False] * n
        for i in range(n):
            cur = 0
            while not visited[i]:
                visited[i] = True
                cur += 1
                i = nums[i]
            res = max(res, cur)
        return res

    # optimize space
    def arrayNesting3(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        for i in range(n):
            cur = 0
            while nums[i] >= 0:
                cur += 1
                nxt = nums[i]
                nums[i] = -1
                i = nxt
            res = max(res, cur)
        return res
