from typing import List
import collections


class Solution:
    def __init__(self):
        self.res = 0

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ss = collections.defaultdict(list)
        for i, v in enumerate(manager):
            ss[v].append(i)

        self.dfs(ss, informTime, headID, 0)
        return self.res

    def dfs(self, ss, informTime, cur, curRes):
        curRes += informTime[cur]
        self.res = max(self.res, curRes)

        for s in ss[cur]:
            self.dfs(ss, informTime, s, curRes)
