import heapq
from typing import List
import collections


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq, visited, res = [(0, K)], set(), 0
        while pq:
            w, v = heapq.heappop(pq)
            if v in visited:
                continue

            visited.add(v)
            res = max(res, w)
            for nv, nw in graph[v]:
                if nv not in visited:
                    heapq.heappush(pq, (nw + w, nv))

        return res if len(visited) == N else -1
