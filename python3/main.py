import heapq
import functools
from typing import List
import itertools
import collections
import math
import random
import bisect
from python3.common.define import TreeNode
from functools import reduce
import operator
import functools

from functools import reduce, lru_cache
import operator


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        m, sc = len(paths), None
        dt = [collections.defaultdict(list) for _ in range(m)]
        for i, path in enumerate(paths):
            for j, c in enumerate(path):
                dt[i][c].append(j)

            if sc is None or len(paths[sc]) > len(paths[i]):
                sc = i

        def helper(si, j, ll):
            c, mcl = paths[sc][si], 0
            for k in dt[j][c]:
                cl = 1
                while cl < ll and k + cl < len(paths[j]) and paths[sc][si + cl] == paths[j][k + cl]:
                    cl += 1
                mcl = max(mcl, cl)
                if mcl == ll:
                    return ll
            return mcl

        res = 0
        for i in range(len(paths[sc])):
            ll = len(paths[sc]) - i
            for j in range(m):
                if j == sc:
                    continue

                ll = helper(i, j, ll)
                if ll == len(paths[sc]) - i:
                    break

            res = max(res, ll)
            if res >= len(paths[sc]) - i:
                break

        return res
if __name__ == '__main__':
    Solution().longestCommonSubpath(
        5,
        [[0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 3, 0, 1, 4, 0, 1, 0]],
    )
