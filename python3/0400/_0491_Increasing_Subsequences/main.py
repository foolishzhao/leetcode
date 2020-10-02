from typing import List
import collections


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        dt = collections.defaultdict(list)
        for i, cur in enumerate(nums):
            dt[i].append([cur])
            for j, prev in enumerate(nums[:i]):
                if cur >= prev:
                    for v in dt[j]:
                        dt[i].append(v + [cur])

        res = set()
        for u in dt.values():
            for v in u:
                if len(v) > 1:
                    res.add(tuple(v))

        return [list(x) for x in res]

    def findSubsequences2(self, nums: List[int]) -> List[List[int]]:
        res = set()
        self.dfs(res, list(), nums, 0)
        return list(res)

    def dfs(self, res, curRes, nums, pos):
        if len(curRes) >= 2:
            res.add(tuple(curRes))

        for i in range(pos, len(nums)):
            if not curRes or nums[i] >= curRes[-1]:
                self.dfs(res, curRes + [nums[i]], nums, i + 1)
