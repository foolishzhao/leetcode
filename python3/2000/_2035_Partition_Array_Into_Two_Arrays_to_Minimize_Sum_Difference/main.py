from typing import List
import bisect


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def getPar(arr):
            par = [list() for _ in range(n + 1)]
            dfs(arr, par, 0, 0, 0)
            for p in par:
                p.sort()
            return par

        def dfs(arr, par, pos, cur, bit):
            if pos == n:
                par[bit].append(cur)
                return

            dfs(arr, par, pos + 1, cur + arr[pos], bit + 1)
            dfs(arr, par, pos + 1, cur, bit)

        n, s = len(nums) // 2, sum(nums)
        par1, par2 = getPar(nums[:n]), getPar(nums[n:])

        res = float('inf')
        for i in range(n + 1):
            j = n - i
            for p1 in par1[i]:
                idx = bisect.bisect_left(par2[j], s / 2 - p1)
                if idx < len(par2[j]):
                    p2 = par2[j][idx]
                    res = min(res, abs(s - 2 * (p1 + p2)))
                if idx > 0:
                    p2 = par2[j][idx - 1]
                    res = min(res, abs(s - 2 * (p1 + p2)))
        return res
