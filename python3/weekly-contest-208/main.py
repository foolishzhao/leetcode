import heapq
import functools
from typing import List
import collections
import math
import random
import bisect
import functools
from python3.common.define import TreeNode


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res, transfer = 0, collections.defaultdict(int)
        for fr, to in requests:
            if fr == to:
                res += 1
            else:
                transfer[(fr, to)] += 1

        def dfs(par, u, p):
            p.append(u)
            if u == par:
                return True

            for v in range(n):
                if transfer[(u, v)] > 0 and (v == par or v not in p):
                    if dfs(par, v, p):
                        return True
            return False

        for fr in range(n):
            for to in range(n):
                while transfer[(fr, to)] > 0:
                    path = [fr]
                    if dfs(fr, to, path):
                        for u, v in zip(path[:-1], path[1:]):
                            res += 1
                            transfer[(u, v)] -= 1
                    else:
                        break
        return res


if __name__ == '__main__':
    print(Solution().maximumRequests(
        3,
        [[1, 2], [2, 2], [0, 0], [1, 1], [0, 2], [0, 0], [2, 1], [0, 1], [1, 0], [2, 2], [0, 1], [2, 0], [2, 2]],
    ))
