from typing import List
import collections


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        neighbor, edges = collections.defaultdict(int), set()
        for u, v in roads:
            neighbor[u] += 1
            neighbor[v] += 1
            edges.add((min(u, v), max(u, v)))

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, neighbor[i] + neighbor[j] - ((i, j) in edges))
        return res
