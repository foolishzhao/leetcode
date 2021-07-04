from scipy.special import comb
from typing import List
import collections


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:

        def dfs(u):
            res, cs = 1, list()
            for v in child[u]:
                subRes, vc = dfs(v)
                res *= subRes
                res %= (10 ** 9 + 7)
                cs.append(vc)

            t = sum(cs)
            for c in cs:
                res = res * comb(t, c, exact=True) % (10 ** 9 + 7)
                t -= c

            return res, sum(cs) + 1

        child = collections.defaultdict(list)
        for i, prev in enumerate(prevRoom):
            child[prev].append(i)

        res, _ = dfs(0)
        return res
